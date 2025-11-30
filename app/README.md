# 📅 Haftalık Planlayıcı AI - Polaris Alpha

OpenRouter'ın Polaris-Alpha modeli ile çalışan akıllı haftalık planlama asistanı.

## 🎯 Özellikler

- **Akıllı Planlama**: Görevlerinizi analiz eder ve en uygun haftalık planı oluşturur
- **Öncelik Yönetimi**: Yüksek, orta, düşük öncelikli görevleri ayırır
- **Enerji Seviyesi Optimizasyonu**: Hangi saatlerde daha verimli olduğunuzu dikkate alır
- **Sohbet Tabanlı**: Doğal dille konuşarak planınızı oluşturun
- **Detaylı Planlama**: Saatlik görev dağılımı ve mola zamanları
- **Gerçekçi Süre Tahminleri**: Görevleri sıkıştırmadan, uygulanabilir planlar

## 🚀 Nasıl Çalışır?

1. **Bilgi Toplama**: AI asistan size sorular sorar:
   - Yapmanız gereken görevler
   - Her görevin tahmini süresi
   - Öncelik seviyeleri
   - Çalışma saatleri ve müsaitlik
   - Enerji seviyeleri (sabah/akşam)
   - Özel kısıtlamalar

2. **Plan Oluşturma**: Topladığı bilgilere göre:
   - Pazartesi-Pazar detaylı plan
   - Saatlik görev dağılımı
   - Mola zamanları
   - Öncelik sıralaması

3. **Optimizasyon**: Plan şunları içerir:
   - Deep work için benzer görevlerin gruplanması
   - Enerji seviyesine göre görev yerleştirme
   - Esnek zaman blokları
   - Acil durum tampon zamanları

## 📋 Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install Flask requests
```

2. Uygulamayı başlatın:
```bash
python app.py
```

3. Tarayıcınızda açın:
```
http://127.0.0.1:5001
```

## 🔑 API Key

OpenRouter API key'inizi [buradan](https://openrouter.ai/keys) alabilirsiniz.

## 💡 Kullanım Örneği

**Kullanıcı**: "Bu hafta 3 proje teslimim var, bir sunum hazırlamam lazım ve spor yapmak istiyorum. Yardım eder misin?"

**AI Asistan**:
- Hangi projeler, her biri kaç saat sürer?
- Sunum ne hakkında, hazırlık süresi?
- Spor için hangi günler uygun?
- Sabah mı akşam mı daha verimlisiniz?
- ... (diğer sorular)

**Sonuç**: Detaylı haftalık plan hazırlanır.

## 🎨 Özellikler

- Modern ve temiz arayüz
- Gerçek zamanlı sohbet
- Yazma animasyonu
- Mobil uyumlu tasarım
- Kolay API key yönetimi

## 🤖 Model: OpenRouter Polaris-Alpha

Polaris-Alpha, haftalık planlama için optimize edilmiş gelişmiş bir modeldir:
- Doğal dil anlama
- Akıllı öneri sistemleri
- Kişiselleştirilmiş planlama
- Detaylı analiz yetenekleri

## 📝 Notlar

- Her sohbet bağımsızdır (session tabanlı değil)
- API key güvenli şekilde saklanır (client-side)
- Plan formatı kolay okunabilir
- İstediğiniz zaman planı güncelleyebilirsiniz

## 🔧 Teknik Detaylar

- **Backend**: Flask (Python)
- **Frontend**: Vanilla JavaScript
- **API**: OpenRouter (Polaris-Alpha)
- **Port**: 5001
