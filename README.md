# Régression Linéaire - Guide de Test de l'Interface Web

## 📋 Description du Projet

Application web de **régression linéaire** développée avec **Django** et **TensorFlow/Keras**. 
L'application utilise un modèle de machine learning entraîné pour prédire des valeurs basées sur des entrées utilisateur.

### Fonctionnalités
- Interface web moderne et responsive
- Prédiction en temps réel via un modèle TensorFlow
- Design technique avec thème sombre personnalisé
- Formulaire interactif pour saisir des paramètres


---

## Installation

### 1. Activer l'Environnement Virtuel

L'environnement virtuel est déjà créé dans le dossier `env/`.

**Sur Linux/macOS:**
```bash
source env/bin/activate
```

### 2. Vérifier l'Installation des Dépendances

```bash
pip list
```

Vérifiez la présence de:
- Django (6.0.7+)
- tensorflow
- keras
- numpy
- h5py (pour charger les modèles Keras)


### 3. Accéder à l'Interface Web

Ouvrez votre navigateur et accédez à:
```
http://54.242.61.15
```

---

## Guide de Test de l'Interface Web

### Phase 1: Test du Chargement de la Page

#### Test 1.1 - Accueil
1. **Action:** Accédez à `http://localhost:8000/`
2. **Attendu:**
   - La page se charge sans erreur
   - Le titre "Régression linéaire" s'affiche
   - Le design technique avec grille est visible
   - L'interface est responsive

#### Test 1.2 - Éléments Visuels
1. **Panneau gauche (Dashboard):**
   - Affichage du logo/indicateur visuel (◆ TECHNICIEN)
   - Titre "RÉGRESSION LINÉAIRE"
   - Zone de jauge/résultat
   - Indicateurs techniques

2. **Panneau droit (Formulaire):**
   - Titre "SAISIE DES PARAMÈTRES"
   - Champs de saisie pour les entités
   - Bouton "PRÉDIRE"
   - Note/instruction d'utilisation

---

### Phase 2: Test du Formulaire

#### Test 2.1 - Affichage du Formulaire
1. **Action:** Inspectez les champs du formulaire
2. **Attendu:**
   - Au minimum 7 champs de saisie (Cylindres, Déplacement, Puissance, Poids, Accélération, Année du modèle, Origine)
   - Chaque champ a un label descriptif
   - Les champs acceptent les entrées numériques

#### Test 2.2 - Validation des Entrées
1. **Action:** Essayez d'entrer des valeurs invalides
   - Laissez des champs vides
   - Entrez du texte au lieu de nombres
   - Entrez des nombres négatifs
   - Entrez des nombres très grands (ex: 999999)

2. **Attendu:**
   - Le formulaire accepte les nombres entiers positifs
   - Les valeurs invalides sont rejetées ou converties

---

### Phase 3: Test des Prédictions

#### Test 3.1 - Prédiction Simple
1. **Action:** Remplissez le formulaire avec les valeurs suivantes:
   ```
   Cylindres:       8
   Déplacement:     307
   Puissance:       130
   Poids:           3504
   Accélération:    12
   Année du modèle: 70
   Origine:         1
   ```

2. **Attendu:**
   - Le bouton "PRÉDIRE" reste cliquable
   - Après le clic, la page se rafraîchit
   - Un résultat (nombre) s'affiche dans la jauge
   - Pas d'erreur 500 ou 404

#### Test 3.2 - Prédictions Multiples
1. **Action:** Effectuez 5 prédictions consécutives avec des valeurs différentes

   **Jeu de données 1:**
   ```
   Cylindres: 4, Déplacement: 120, Puissance: 80, Poids: 2200, 
   Accélération: 15, Année: 75, Origine: 1
   ```

   **Jeu de données 2:**
   ```
   Cylindres: 6, Déplacement: 200, Puissance: 100, Poids: 2800,
   Accélération: 13, Année: 80, Origine: 2
   ```

   **Jeu de données 3:**
   ```
   Cylindres: 3, Déplacement: 79, Puissance: 60, Poids: 1850,
   Accélération: 8, Année: 77, Origine: 3
   ```

2. **Attendu:**
   - Chaque prédiction retourne une valeur différente
   - Les valeurs sont cohérentes (entre 10 et 50 généralement pour MPG)
   - Aucun ralentissement ou freeze

#### Test 3.3 - Cas Limite
1. **Valeurs minimales:**
   ```
   Tous les champs: 1
   ```

2. **Valeurs maximales:**
   ```
   Cylindres: 8, Déplacement: 500, Puissance: 450, Poids: 5000,
   Accélération: 25, Année: 82, Origine: 3
   ```

3. **Attendu:**
   - Les deux cas retournent des prédictions
   - Pas d'erreur ou de crash

---

### Phase 4: Test de Responsivité

#### Test 4.1 - Adaptabilité Mobile
1. **Action:** Redimensionnez la fenêtre du navigateur
   - Desktop (1920px)
   - Tablette (768px)
   - Mobile (375px)

2. **Attendu:**
   - Grille passe à une colonne en dessous de 860px
   - Tous les éléments restent lisibles
   - Formulaire reste utilisable
   - Pas de débordement horizontal

#### Test 4.2 - Test sur Appareil Mobile
1. **Action:** Ouvrez sur téléphone: `http://54.242.61.15/`

2. **Attendu:**
   - Interface s'affiche correctement
   - Touches/champs sont accessibles
   - Prédictions fonctionnent

---

### Phase 5: Test de Performance

#### Test 5.1 - Temps de Chargement Initial
1. **Action:** F5 ou Ctrl+R pour recharger
2. **Attendu:**
   - Page se charge en moins de 2 secondes
   - Pas d'erreurs console

#### Test 5.2 - Temps de Prédiction
1. **Action:** Mesurez le temps entre le clic et le résultat
2. **Attendu:**
   - Prédiction < 1 seconde
   - Interface réactive

#### Test 5.3 - Prédictions Rapides
1. **Action:** Effectuez 10 prédictions consécutives rapidement
2. **Attendu:**
   - Pas d'erreur 429 (Too Many Requests)
   - Pas de ralentissement
   - Serveur reste stable

---

### Phase 6: Test du Modèle

#### Test 6.1 - Vérification du Modèle Keras
1. **Action:** Dans une console Python, exécutez:
```python
import tensorflow as tf
model = tf.keras.models.load_model("regression/models/predict.keras")
print(model.summary())
```

2. **Attendu:**
   - Modèle se charge sans erreur
   - Affichage de l'architecture (couches, paramètres)
   - Input shape clairement défini

#### Test 6.2 - Compatibilité des Entrées
1. **Action:** Vérifiez que le nombre d'entrées du formulaire correspond au modèle

2. **Attendu:**
   - Si le modèle attend 7 paramètres → 7 champs dans le formulaire
   - Correspondance exacte entre entrées et features du modèle



---

## Checklist de Test Complet

| # | Test | Statut | Notes |
|---|------|--------|-------|
| 1.1 | Page d'accueil se charge | ☐ | |
| 1.2 | Éléments visuels présents | ☐ | |
| 2.1 | Formulaire affiche tous les champs | ☐ | |
| 2.2 | Validation des entrées | ☐ | |
| 3.1 | Prédiction simple | ☐ | |
| 3.2 | 5 prédictions différentes | ☐ | |
| 3.3 | Cas limites | ☐ | |
| 4.1 | Adaptabilité mobile (resize) | ☐ | |
| 4.2 | Test sur téléphone | ☐ | |
| 5.1 | Temps de chargement | ☐ | |
| 5.2 | Temps de prédiction | ☐ | |
| 5.3 | 10 prédictions rapides | ☐ | |
| 6.1 | Modèle se charge | ☐ | |
| 6.2 | Nombre d'entrées correct | ☐ | |
| 7.1 | Erreur 404 | ☐ | |
| 7.2 | Serveur déconnecté | ☐ | |
| 7.3 | POST directe | ☐ | |

---


```
regression_lineaire/
├── manage.py                 # Gestionnaire Django
├── README.md                 # Ce fichier
├── db.sqlite3               # Base de données
├── regression_lineaire/
│   ├── settings.py          # Configuration Django
│   ├── urls.py              # Routage des URLs
│   └── wsgi.py              # Interface WSGI
├── regression/
│   ├── views.py             # Logique des vues
│   ├── models.py            # Modèles de données
│   ├── processing.py        # Script d'entraînement
│   ├── templates/
│   │   └── index.html       # Interface web
│   └── models/
│       └── predict.keras    # Modèle TensorFlow
└── static/                  # Fichiers statiques (CSS, JS, images)
```


**Dernière mise à jour:** 2026-07-16  
**Version:** 1.0  
**Auteur:** Machine Learning - Master 1 EPT
