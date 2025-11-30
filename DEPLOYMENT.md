# 🚀 Ücretsiz Hosting Kurulum Rehberi

## 📋 Hazırlık (Tamamlandı ✅)

Aşağıdaki dosyalar deployment için oluşturuldu:
- ✅ `Procfile` - Render için başlatma komutu
- ✅ `runtime.txt` - Python versiyonu
- ✅ `render.yaml` - Render konfigürasyonu
- ✅ `requirements.txt` - Gunicorn eklendi
- ✅ `app/app.py` - Production optimizasyonları yapıldı

---

## 🌐 Render.com ile Ücretsiz Deployment (ÖNERİLEN)

### Adım 1: Değişiklikleri GitHub'a Push Et

```bash
cd planner
git add .
git commit -m "Add deployment files for Render"
git push origin main
```

### Adım 2: Render.com'a Kaydol

1. https://render.com adresine git
2. "Get Started for Free" butonuna tıkla
3. GitHub hesabınla giriş yap

### Adım 3: Yeni Web Service Oluştur

1. Dashboard'da "New +" butonuna tıkla
2. "Web Service" seç
3. GitHub reponuzu bağla (planner)
4. Repoyu seç ve "Connect" tıkla

### Adım 4: Konfigürasyon

Render otomatik olarak ayarları algılayacak, şunları kontrol et:

- **Name**: `planner-app` (veya istediğin isim)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app.app:app`
- **Plan**: `Free` seçili olsun

### Adım 5: Environment Variables (Opsiyonel)

"Advanced" bölümünde ortam değişkenleri ekle:

- **SITE_URL**: `https://[senin-app-adin].onrender.com` (deploy edildikten sonra ekleyebilirsin)

### Adım 6: Deploy!

1. "Create Web Service" butonuna bas
2. 5-10 dakika bekle (ilk deployment biraz uzun sürer)
3. Ücretsiz domain'in hazır: `https://[senin-app-adin].onrender.com`

---

## 🎯 Alternatif Seçenekler

### PythonAnywhere

1. https://www.pythonanywhere.com adresine git
2. Ücretsiz hesap oluştur
3. "Web" sekmesine git
4. "Add a new web app" tıkla
5. Flask seç ve repoyu clone et

**Ücretsiz Domain**: `username.pythonanywhere.com`

### Railway

1. https://railway.app adresine git
2. GitHub ile giriş yap
3. "New Project" → "Deploy from GitHub repo"
4. planner reposunu seç
5. Otomatik deploy başlar

**Ücretsiz Tier**: $5 credit/ay

### Fly.io

```bash
# Fly CLI kur
# Windows için:
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"

# Login ol
fly auth login

# Deploy et
fly launch
fly deploy
```

---

## 🔑 Önemli Notlar

### OpenRouter API Key

Uygulamanız OpenRouter API kullanıyor. Kullanıcılar kendi API key'lerini arayüzde girecekler, bu yüzden ekstra ayar gerekmez.

### Ücretsiz Tier Limitleri

**Render.com**:
- ✅ 512MB RAM
- ✅ Sınırsız bandwidth
- ⚠️ 15 dakika hareketsizlikten sonra uyur (ilk istek 30 saniye sürebilir)
- ✅ SSL sertifikası dahil

**PythonAnywhere**:
- ✅ 512MB disk
- ⚠️ Günlük CPU limiti var
- ⚠️ HTTPS sadece ücretli planda

**Railway**:
- ✅ $5 credit/ay
- ⚠️ Credit bitince durdurulur

---

## 🆓 Ücretsiz Domain Alma (Opsiyonel)

Kendi domain'inizi istiyorsanız:

### Freenom (Ücretsiz)

1. https://www.freenom.com adresine git
2. Ücretsiz domain al (.tk, .ml, .ga, .cf, .gq)
3. Render'da "Custom Domain" bölümünden domain ekle
4. DNS ayarlarını Render'ın verdiği şekilde güncelle

### Alternatif: Ücretsiz Subdomain

- https://freedns.afraid.org
- https://www.noip.com

---

## 🧪 Test Etmek İçin

Deploy edildikten sonra:

1. `https://[senin-app-adin].onrender.com` adresine git
2. OpenRouter API key'ini gir
3. Haftalık plan oluşturmayı dene

---

## ❓ Sorun Giderme

### "Application failed to start"

1. Render loglarını kontrol et
2. `requirements.txt` dosyasının doğru olduğundan emin ol
3. Python versiyonunu kontrol et

### "ModuleNotFoundError"

Build command'da `pip install -r requirements.txt` olduğundan emin ol

### API Hatası

OpenRouter API key'in geçerli olduğundan emin ol: https://openrouter.ai/keys

---

## 📞 Yardım

- Render Docs: https://render.com/docs
- PythonAnywhere Help: https://help.pythonanywhere.com

**Başarılar! 🎉**
