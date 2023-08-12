import pandas as pd

# Charger le dataset
df = pd.read_csv('dataset-tortuga-filled.csv')

def determine_favorite(row):
    """Détermine le cours favori en fonction des heures et des scores."""
    # Récupérer les heures et les scores pour chaque matière
    hours_data = row['HOURS_DATASCIENCE']
    score_data = row['AVG_SCORE_DATASCIENCE']
    
    hours_back = row['HOURS_BACKEND']
    score_back = row['AVG_SCORE_BACKEND']
    
    hours_front = row['HOURS_FRONTEND']
    score_front = row['AVG_SCORE_FRONTEND']
    
    # Calculer une "préférence" en multipliant les heures par les scores
    preference_data = hours_data * score_data
    preference_back = hours_back * score_back
    preference_front = hours_front * score_front
    
    # Trouver le cours avec la préférence la plus élevée
    max_pref = max(preference_data, preference_back, preference_front)
    
    if max_pref == preference_data:
        return "DATASCIENCE"
    elif max_pref == preference_back:
        return "BACKEND"
    else:
        return "FRONTEND"

def determine_hated(row):
    """Détermine le cours détesté en fonction des heures et des scores."""
    # Logique similaire à la fonction de dessus, mais en cherchant le minimum
    hours_data = row['HOURS_DATASCIENCE']
    score_data = row['AVG_SCORE_DATASCIENCE']
    
    hours_back = row['HOURS_BACKEND']
    score_back = row['AVG_SCORE_BACKEND']
    
    hours_front = row['HOURS_FRONTEND']
    score_front = row['AVG_SCORE_FRONTEND']
    
    preference_data = hours_data * score_data
    preference_back = hours_back * score_back
    preference_front = hours_front * score_front
    
    min_pref = min(preference_data, preference_back, preference_front)
    
    if min_pref == preference_data:
        return "DATASCIENCE"
    elif min_pref == preference_back:
        return "BACKEND"
    else:
        return "FRONTEND"


# Appliquer les fonctions pour créer les nouvelles colonnes FAV_COURS et HAT_COURS
df['FAV_COURS'] = df.apply(determine_favorite, axis=1)
df['HAT_COURS'] = df.apply(determine_hated, axis=1)


# Enregistrer le DataFrame modifié
df.to_csv('dataset-tortuga-filled-modified2.csv', index=False)

#______________________________________________________________________________________________________________________________
#update column Profile

import pandas as pd

# Chargement du dataset
df = pd.read_csv('dataset-tortuga-filled-modified2.csv')

def determine_profile(row):
    # Pour chaque matière, combinez les heures, scores et nombre de cours pour obtenir un score global
    score_data = row['HOURS_DATASCIENCE'] + row['AVG_SCORE_DATASCIENCE'] + (row['NUM_COURSES_BEGINNER_DATASCIENCE'] + row['NUM_COURSES_ADVANCED_DATASCIENCE']) * 10
    score_back = row['HOURS_BACKEND'] + row['AVG_SCORE_BACKEND'] + (row['NUM_COURSES_BEGINNER_BACKEND'] + row['NUM_COURSES_ADVANCED_BACKEND']) * 10
    score_front = row['HOURS_FRONTEND'] + row['AVG_SCORE_FRONTEND'] + (row['NUM_COURSES_BEGINNER_FRONTEND'] + row['NUM_COURSES_ADVANCED_FRONTEND']) * 10

    # Identifiez la matière avec le score le plus élevé
    max_subject = max([('data', score_data), ('back', score_back), ('front', score_front)], key=lambda x: x[1])[0]

    if max_subject == 'data':
        if row['NUM_COURSES_BEGINNER_DATASCIENCE'] >= 2:
            return 'beginner_data_science'
        elif row['NUM_COURSES_ADVANCED_DATASCIENCE'] >= 2:
            return 'advanced_data_science'
        else:
            return 'intermediate_data_science'
    elif max_subject == 'back':
        if row['NUM_COURSES_BEGINNER_BACKEND'] >= 2:
            return 'beginner_back_end'
        elif row['NUM_COURSES_ADVANCED_BACKEND'] >= 2:
            return 'advanced_back_end'
        else:
            return 'intermediate_back_end'
    elif max_subject == 'front':
        if row['NUM_COURSES_BEGINNER_FRONTEND'] >= 2:
            return 'beginner_front_end'
        elif row['NUM_COURSES_ADVANCED_FRONTEND'] >= 2:
            return 'advanced_front_end'
        else:
            return 'intermediate_front_end'

# Appliquer la fonction pour mettre à jour la colonne PROFILE
df['PROFILE'] = df.apply(determine_profile, axis=1)

# Enregistrement des modifications
df.to_csv('dataset-tortuga-filled-modified3.csv', index=False)

#____________________________________________________________________________________________________________________

import pandas as pd
import numpy as np

# Charger le dataset
df = pd.read_csv('dataset-tortuga-filled-modified3.csv')

# ---- GÉNÉRATION DES DONNÉES POUR LES NOUVELLES MATIÈRES ----

# Utiliser une graine pour assurer la reproductibilité des nombres aléatoires
np.random.seed(42)

# Générer des données pour les heures passées sur IA et BDD
# En supposant que les heures pour IA et BDD sont liées aux heures de DATASCIENCE et BACKEND respectivement
df['HOURS_IA'] = df['HOURS_DATASCIENCE'] * np.random.rand(len(df))
df['HOURS_BDD'] = df['HOURS_BACKEND'] * np.random.rand(len(df))

# Générer aléatoirement le nombre de cours beginner et advanced pour IA
df['NUM_COURSES_BEGINNER_IA'] = np.random.randint(0, 3, len(df))
df['NUM_COURSES_ADVANCED_IA'] = np.random.randint(0, 3, len(df))

# Générer aléatoirement le nombre de cours beginner et advanced pour BDD
df['NUM_COURSES_BEGINNER_BDD'] = np.random.randint(0, 3, len(df))
df['NUM_COURSES_ADVANCED_BDD'] = np.random.randint(0, 3, len(df))

# Générer les scores moyens pour IA et BDD en se basant sur les scores de DATASCIENCE et BACKEND
df['AVG_SCORE_IA'] = df['AVG_SCORE_DATASCIENCE'] * np.random.rand(len(df))
df['AVG_SCORE_BDD'] = df['AVG_SCORE_BACKEND'] * np.random.rand(len(df))

# ---- DÉTERMINATION DU PROFIL ----

# Fonction pour déterminer le profil en fonction des heures, scores, et nombre de cours assistés
def determine_profile(row):
    subjects = ['DATASCIENCE', 'BACKEND', 'FRONTEND', 'IA', 'BDD']
    
    hours = [row[f'HOURS_{subject}'] for subject in subjects]
    scores = [row[f'AVG_SCORE_{subject}'] for subject in subjects]
    combined = [score + hour for score, hour in zip(scores, hours)]
    
    max_index = np.argmax(combined)
    
    if "BEGINNER" in row and row[f'NUM_COURSES_BEGINNER_{subjects[max_index]}'] > 0:
        return f"beginner_{subjects[max_index].lower()}"
    elif "ADVANCED" in row and row[f'NUM_COURSES_ADVANCED_{subjects[max_index]}'] > 0:
        return f"advanced_{subjects[max_index].lower()}"
    else:
        return f"intermediate_{subjects[max_index].lower()}"

# Appliquer la fonction pour déterminer le profil
df['PROFILE'] = df.apply(determine_profile, axis=1)

# ---- DÉTERMINATION DU COURS FAVORI ET DÉTESTÉ ----

# Fonction pour déterminer le cours favori et détesté basé sur scores, heures, et nombre de cours
def favorite_course(row):
    subjects = ['DATASCIENCE', 'BACKEND', 'FRONTEND', 'IA', 'BDD']
    scores = [row[f'AVG_SCORE_{subject}'] for subject in subjects]
    hours = [row[f'HOURS_{subject}'] for subject in subjects]
    
    combined_score = [score + hour for score, hour in zip(scores, hours)]
    fav_course = subjects[np.argmax(combined_score)]
    hated_course = subjects[np.argmin(combined_score)]
    
    return fav_course, hated_course

df['FAV_COURS'], df['HAT_COURS'] = zip(*df.apply(favorite_course, axis=1))

# Sauvegarder le dataset modifié
df.to_csv('dataset-tortuga-filled-modified.csv4', index=False)





