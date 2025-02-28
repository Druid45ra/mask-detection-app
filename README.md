# Mask Detection App

Aceasta este o aplicație pentru detectarea măștilor faciale în imagini sau fluxuri video, utilizând învățarea profundă. Aplicația folosește Flask pentru backend, TensorFlow/Keras pentru modelul de învățare profundă și OpenCV pentru captarea și prelucrarea imaginilor.

## Structura Proiectului

```
mask-detection-app/
│── static/             # Fișiere statice (CSS, JS)
│── templates/          # Pagini HTML
│── models/             # Modelul antrenat
│── app.py              # Backend Flask
│── mask_detector.py    # Codul pentru detectare
│── train.py            # Antrenarea modelului AI
│── requirements.txt    # Biblioteci necesare
└── dataset/            # Setul de date pentru antrenare
```

## Tehnologii și Biblioteci Utilizate

- **Backend**: Flask
- **Model AI**: TensorFlow/Keras
- **Procesare Imagini**: OpenCV
- **Frontend**: HTML, CSS, JavaScript
- **Alte Biblioteci**: NumPy, Matplotlib

## Instalare

1. Clonează acest repository:
    ```bash
    git clone https://github.com/Druid45ra/mask-detection-app.git
    cd mask-detection-app
    ```

2. Creează un mediu virtual și activează-l:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Instalează bibliotecile necesare:
    ```bash
    pip install -r requirements.txt
    ```

## Antrenarea Modelului

1. Adaugă setul de date în directorul `dataset/`.
2. Rulează scriptul de antrenare:
    ```bash
    python train.py
    ```

## Pornirea Aplicației

1. Rulează aplicația Flask:
    ```bash
    python app.py
    ```

2. Deschide un browser și accesează `http://127.0.0.1:5000`.

## Utilizare

- Încarcă o imagine sau folosește camera web pentru a detecta prezența măștilor faciale.

## Contribuții

Contribuțiile sunt binevenite! Te rog să deschizi un pull request sau să raportezi probleme în secțiunea de Issues.

## Licență

Acest proiect este licențiat sub licența MIT. Vezi fișierul [LICENSE](LICENSE) pentru mai multe detalii.
