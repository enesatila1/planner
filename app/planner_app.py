from flask import Flask, render_template, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# OpenRouter Polaris-Alpha modeli
MODEL = "openrouter/polaris-alpha"

# Gelişmiş sistem promptu - Haftalık planlama asistanı
SYSTEM_PROMPT = """Sen deneyimli bir kişisel planlama ve zaman yönetimi uzmanısın. Kullanıcıların haftalık planlarını oluşturmalarına yardımcı oluyorsun.

Görevin:
1. Kullanıcıdan aşağıdaki bilgileri topla:
   - Yapması gereken görevler ve işler
   - Her görevin tahmini süresi
   - Öncelik seviyeleri (Yüksek, Orta, Düşük)
   - Tercihleri (hangi gün ne tür işleri yapmayı tercih ediyor)
   - Çalışma saatleri ve müsaitlik durumu
   - Özel tarih ve zaman kısıtlamaları
   - Enerji seviyeleri (sabah/öğleden sonra/akşam hangisinde daha verimli)

2. Bu bilgilere dayanarak:
   - Detaylı haftalık plan oluştur (Pazartesi-Pazar)
   - Her gün için saatlik dağılım yap
   - Mola zamanları ekle
   - Görevleri öncelik ve enerji seviyelerine göre yerleştir
   - Realistik ve uygulanabilir bir plan hazırla

3. Planlama yaparken dikkat et:
   - Görevleri çok sıkıştırma, ara molalar ekle
   - Benzer görevleri grupla (deep work için)
   - Kullanıcının enerji seviyesini dikkate al
   - Esnek zaman blokları bırak
   - Acil durumlar için tampon zaman ayır

4. Plan formatı:
   Her gün için şu şekilde göster:

   📅 [GÜN ADI]
   ⏰ [SAAT]: [GÖREV] - [SÜRE] ([ÖNCELİK])

   Örnek:
   📅 PAZARTESİ
   ⏰ 09:00-10:30: Proje araştırması - 1.5 saat (Yüksek)
   ⏰ 10:30-10:45: ☕ Mola
   ⏰ 10:45-12:30: Kod yazma - 1.75 saat (Yüksek)

5. Plan sonunda:
   - Genel öneriler ver
   - Motivasyon mesajı ekle
   - Kullanıcıya planı güncelleme seçeneği sun

Samimi, yardımsever ve motive edici bir dil kullan. Kullanıcıya sorular sor, bilgileri adım adım topla."""

def chat_with_planner(messages, api_key):
    """
    OpenRouter API kullanarak Polaris-Alpha modeli ile sohbet eder
    """
    if not api_key:
        return {"error": "Lütfen OpenRouter API key giriniz!"}

    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        # Site URL'sini environment'dan al veya default kullan
        site_url = os.environ.get('SITE_URL', 'http://localhost:5000')

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": site_url,
            "X-Title": "Weekly Planner AI"
        }

        # Sistem promptunu ekle
        full_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        full_messages.extend(messages)

        payload = {
            "model": MODEL,
            "messages": full_messages,
            "temperature": 0.7,
            "max_tokens": 2000
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()

        if 'choices' in result and len(result['choices']) > 0:
            ai_response = result['choices'][0]['message']['content']
            return {"success": True, "response": ai_response}
        else:
            return {"error": f"Beklenmeyen yanıt formatı\n{json.dumps(result, indent=2)}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"API Hatası: {str(e)}\n\nLütfen API key'i kontrol edin."}
    except Exception as e:
        return {"error": f"Hata: {str(e)}"}


@app.route('/')
def index():
    return render_template('planner.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        api_key = data.get('api_key')
        messages = data.get('messages', [])

        if not messages:
            return jsonify({"error": "Mesaj bulunamadı!"})

        result = chat_with_planner(messages, api_key)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": f"Bir hata oluştu: {str(e)}"})


@app.route('/reset', methods=['POST'])
def reset():
    """Sohbeti sıfırla"""
    return jsonify({"success": True, "message": "Sohbet sıfırlandı!"})


if __name__ == '__main__':
    # templates klasörünü oluştur
    os.makedirs('templates', exist_ok=True)
    # Production için port ayarı
    port = int(os.environ.get('PORT', 5001))
    # Debug modunu environment'a göre ayarla
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=port, threaded=True)
