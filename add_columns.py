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





