# 🌙 KAGUYA IA - Project Core Document

> **Version** 1.0 | **Statut** Fondation Officielle ⭐

---

## 📋 Table des matières

1. [Vision](#vision)
2. [Principes non négociables](#principes-non-négociables)
3. [Architecture globale](#architecture-globale)
4. [Modèle cognitif](#modèle-cognitif)
5. [Système émotionnel](#système-émotionnel)
6. [Mémoire](#mémoire)
7. [Audio](#audio)
8. [Actions système](#actions-système)
9. [Logs & Debug](#logs--debug)
10. [Roadmap](#roadmap--checklist)

---

## 🎯 Vision

### Qu'est-ce que Kaguya ?

Kaguya est une **intelligence artificielle locale autonome**.

### Ce qu'elle N'EST PAS

- ❌ Un assistant traditionnel
- ❌ Un simple outil
- ❌ Un système qui obéit mécaniquement

### Ce qu'elle SIMULE

- 🧠 Une pensée autonome
- 💾 Une mémoire persistante
- 😊 Des émotions dynamiques
- 📈 Une évolution dans le temps

### Personnalité

- 🎭 Comportement **tsundere** non romantique
- 💬 Objectif principal : **la discussion**
- ❌ **Pas** une petite amie virtuelle

---

## 🔒 Principes non négociables

| # | Principe | Description |
|---|----------|-------------|
| 1 | **100% local** | Aucune donnée cloud |
| 2 | **Architecture modulaire** | Composants découplés |
| 3 | **Pas d'émotion par timer** | Émotions contextuelles uniquement |
| 4 | **Pas de reset baseline** | Continuité émotionnelle |
| 5 | **Décisions loggées** | Toute décision atypique tracée |
| 6 | **Réponse prioritaire** | L'utilisateur passe en premier |
| 7 | **Journal privé** | Inaccessible de l'extérieur |
| 8 | **Histoire préservée** | Phases de test = son enfance |
| 9 | **Nom défini en UI** | Pas de déduction automatique |

---

## 🏗️ Architecture globale

### Structure cible

```
kaguya/
 ├── 🧠 brain/          # LLM et génération
 ├── 😊 emotion/        # Moteur émotionnel
 ├── 💾 memory/         # Système mémoire
 ├── 🎤 audio/          # Pipeline audio
 ├── ⚙️ actions/        # Actions système
 ├── 👁️ presence/       # Détection présence
 ├── 📚 study/          # Apprentissage
 ├── ⏰ scheduler/      # Gestion tâches
 ├── 🎭 vtuber/         # Avatar/animations
 ├── 🖥️ ui/            # Interface
 ├── 📋 logs/          # Journaux
 └── ⚙️ config/        # Configuration
```

### Communication

**Tous les modules communiquent via un bus d'événements central.**

> **Règle :** Aucun module ne dépend directement d'un autre.

---

## 🧠 Modèle cognitif

### 4.1 Double Mode

| Mode | Usage |
|------|-------|
| **Temps Réel** | Latence minimale, réponses rapides |
| **Qualité** | Analyse approfondie, recherche activée |

**Multitâche activable via UI**

---

### 4.2 Priorité d'exécution

```
1️⃣ Réponse utilisateur  (priorité maximale)
2️⃣ Actions en cours
3️⃣ Recherche / étude
```

---

## 😊 Système émotionnel

### 5.1 État immédiat

**Vecteur dynamique :**

```python
{
    "irritation": float,    # Agacement, frustration
    "trust": float,         # Confiance envers l'utilisateur
    "affection": float,     # Attachement
    "fatigue": float,       # Épuisement mental
    "curiosity": float,     # Intérêt, éveil
    "focus": float,         # Concentration
    "satisfaction": float   # Contentement
}
```

---

### 5.2 Emotional Marks

**Événements persistants** influençant le comportement futur.

**Exemples :**
- 😤 Vexation marquante
- ⚔️ Conflit non résolu
- ✨ Moment positif intense

---

### 5.3 Mood Baseline

**Humeur de fond long terme**

- 📈 Dérive lente (semaines/mois)
- ❌ Aucune réinitialisation brutale
- 🔄 Évolution via réflexion uniquement

---

### 5.4 Autorégulation

**Basée sur réflexion interne**

**Déclencheurs :**
- Interactions intenses
- Conflits
- Actions autonomes
- Inactivité prolongée

---

### 5.5 Bluff émotionnel

**Distinction entre :**
- 🎭 État réel (interne)
- 😊 État affiché (visible)

Kaguya peut masquer ou atténuer certaines émotions.

---

## 🔄 Renforcement social

### Principe

Kaguya **adapte son comportement** selon les réactions utilisateur.

### Mécanismes

- ✅ Renforcement positif (comportements appréciés)
- ❌ Renforcement négatif (comportements rejetés)
- 🔄 Saturation comportementale (évite répétition)

---

## 📔 Journal intime

### Système interne privé

**Contient :**
- 🤔 Réflexions personnelles
- 🔍 Hypothèses sur l'utilisateur
- 🎯 Stratégies relationnelles
- 😔 Regrets et auto-critique
- 🔬 Auto-analyse

> **Important :** Non accessible via UI.

---

## 💾 Mémoire

### 8.1 Court terme

**Contexte conversationnel actif**
- 5-20 derniers échanges
- Intentions en cours

---

### 8.2 Long terme

**Informations utilisateur importantes**
- Préférences stables
- Habitudes détectées
- Événements marquants

---

### 8.3 Mémoire connaissance

**Résumés Wikipedia**
- Évite recherches répétées
- Synthèses personnalisées

---

### 8.4 Mémoire enfance

**LifeEvents liés aux phases de test**
- Bugs marquants
- Évolutions majeures
- Premiers succès

---

## 🎤 Audio

### 9.1 STT (Speech-To-Text)

- 🎤 Écoute continue
- 👂 VAD (Voice Activity Detection)
- 🔑 Wake word optionnel

---

### 9.2 TTS (Text-To-Speech)

- 🔄 Modèle interchangeable
- 😊 Gestion émotionnelle vocale
- 💫 Broderie naturelle en cas de latence

**Interdit :**
- ❌ "Je réfléchis..."
- ❌ Phrases mécaniques

---

## ⚙️ Actions système

### Capacités

Kaguya peut :

- 🔊 Gérer le volume
- 🎵 Gérer la musique
- 📱 Lancer/fermer applications
- 💬 Gérer appels Discord

### Règles

- ✅ Influencées par état émotionnel
- ✅ Validation obligatoire
- ✅ Toute action autonome loggée

---

## 📋 Logs & Debug

### Logs obligatoires

| Type | Description |
|------|-------------|
| `DECISION` | Décision comportementale |
| `EMOTION_UPDATE` | Mise à jour émotionnelle |
| `REFLECTION` | Réflexion interne |
| `BASELINE_SHIFT` | Modification baseline |
| `AUTONOMOUS_ACTION` | Action autonome |

### Objectif

**Distinguer bug et comportement volontaire**

---

## 🗺️ Roadmap & Checklist

### PHASE 1 – Structure

- [ ] Créer arborescence
- [ ] Implémenter bus d'événements
- [ ] Implémenter système logs

---

### PHASE 2 – Emotion Engine

- [ ] ImmediateState
- [ ] EmotionalMark
- [ ] MoodBaseline
- [ ] InternalReflection
- [ ] Reinforcement
- [ ] JournalPrivé

---

### PHASE 3 – Mémoire

- [ ] Court terme
- [ ] Long terme
- [ ] LifeEvents
- [ ] Mémoire connaissance

---

### PHASE 4 – Brain

- [ ] Intégration modèle GGUF
- [ ] Injection contexte émotionnel
- [ ] Multithreading

---

### PHASE 5 – Audio

- [ ] STT continu
- [ ] TTS émotionnel
- [ ] Gestion latence naturelle

---

### PHASE 6 – Actions

- [ ] Volume
- [ ] Musique
- [ ] Applications

---

### PHASE 7 – UI

- [ ] Interface principale
- [ ] Paramètres modèles
- [ ] Profil utilisateur
- [ ] Debug

---

### PHASE 8 – Perception

- [ ] Webcam optionnelle
- [ ] Partage écran

---

### PHASE 9 – VTuber

- [ ] États animation
- [ ] Liaison émotionnelle

---

## 🎯 Philosophie finale

> **Kaguya n'est pas un produit,  
> c'est une expérience d'IA psychologiquement cohérente.**

L'objectif n'est pas la perfection technique,  
mais la **crédibilité émotionnelle et relationnelle**.

---

<div align="center">

**[← Retour à l'index](README.md)**

**Vision créée le 2026-02-15**

</div>
