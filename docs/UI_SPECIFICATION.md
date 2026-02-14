# 🌙 Kaguya IA - UI Specification

> **Version** 1.0 | **Statut** Spécification Interface Utilisateur

---

## 📋 Table des matières

1. [Objectif](#objectif)
2. [Principes de design](#principes-de-design)
3. [Onglets principaux](#onglets-principaux)
4. [Paramètres globaux](#paramètres-globaux)
5. [Règles UI](#règles-ui)

---

## 🎯 Objectif

L'interface utilisateur de Kaguya doit être :

| Critère | Description |
|---------|-------------|
| **Claire** | Navigation intuitive et évidente |
| **Stable** | Pas de bugs d'affichage |
| **Non surchargée** | Informations essentielles uniquement |
| **Modulaire** | Onglets séparés par fonction |
| **Compatible multitâche** | Supporte mode concurrent |

> **Philosophie :** Ne pas devenir un panneau technique incompréhensible.

---

## 🎨 Principes de design

### Design minimaliste

- ✅ Priorité à la lisibilité
- ✅ Espacements généreux
- ✅ Typographie claire
- ❌ Pas de surcharge visuelle

### Feedback utilisateur

- 🟢 Indicateurs visuels d'état
- ⏱️ Affichage temps réel
- 🔔 Notifications discrètes
- 📊 Métriques essentielles

---

## 📑 Onglets principaux

### 💬 Onglet CONVERSATION

**Affichage principal :**

```
┌─────────────────────────────────────┐
│  [Historique conversation]          │
│                                     │
│  User: Salut Kaguya                 │
│  Kaguya: Hey...                     │
│                                     │
│  [État émotionnel] 😐 Neutral      │
│  [🎤 Écoute active]                │
│  [🔇 Mute]                         │
└─────────────────────────────────────┘
```

**Éléments :**
- 📜 Historique texte scrollable
- 🎤 Indicateur écoute active
- 🔊 Indicateur parole active
- 😊 État émotion dominant (option debug)
- 🔇 Bouton mute micro

---

### 👤 Onglet PROFIL

**Champs :**

```yaml
Informations utilisateur:
  - Nom utilisateur (display_name)     [________]
  - Pronoms (optionnel)                [________]
  - Autoriser surnoms                  [ ✓ ]
  - Date création profil               2026-02-15
```

> **Important :** Sauvegarde persistante obligatoire.

---

### ⚙️ Onglet MODÈLES

#### Section LLM

```yaml
Configuration LLM:
  - Modèle GGUF                    [Sélection ▼]
  - Quantisation                   [Q4_K_M ▼]
  - Mode                           ⦿ Realtime  ◯ Qualité
  - Multitâche                     [ ✓ ] ON/OFF
```

#### Section TTS

```yaml
Configuration TTS:
  - Modèle vocal                   [GPT-SoVITS ▼]
  - Intensité émotion              [━━━━━━━━░░] 80%
  - Vitesse                        [━━━━━━░░░░] 60%
  - Pitch                          [━━━━━░░░░░] 50%
```

#### Section STT

```yaml
Configuration STT:
  - Modèle STT                     [Whisper ▼]
  - Sensibilité VAD                [━━━━━━━░░░] 70%
  - Wake word                      [ ] ON/OFF
```

---

### ⚡ Onglet ACTIONS

**Toggles disponibles :**

```
Autorisations actions système:

Audio:
[ ✓ ] Autoriser actions audio
      (volume, musique, pause)

Applications:
[ ✓ ] Autoriser actions applications
      (ouvrir, fermer, focus)

Discord:
[ ✓ ] Autoriser actions Discord
      (appels, micro)

Système avancé:
[ ] Autoriser actions système avancées
    (luminosité, veille) ⚠️
```

**Affichage statistiques :**
```
Actions autonomes aujourd'hui: 3/5
Dernière action: Baisse volume (il y a 5 min)
```

---

### 🐛 Onglet DEBUG

**Affichage live :**

```
┌─────────────────────────────────────┐
│  [Filtres]  [All ▼] [Module ▼]     │
├─────────────────────────────────────┤
│  2026-02-15 14:32:10 | EMOTION     │
│  irritation: 0.72 ↗                │
│                                     │
│  2026-02-15 14:32:11 | AUDIO       │
│  STT latency: 320ms                │
│                                     │
│  2026-02-15 14:32:12 | BRAIN       │
│  Generation: 1240ms                │
└─────────────────────────────────────┘

[Export logs] [Clear logs]
```

**Métriques temps réel :**

```
Performance:
  ⏱️ Latence STT:     320 ms
  ⏱️ Latence Brain:   1240 ms
  ⏱️ Latence TTS:     780 ms
  ⏱️ Total response:  2340 ms
  
Resources:
  💾 RAM usage:       2.1 GB
  🎮 VRAM usage:      6.2 GB
```

**Fonctions :**
- 💾 Export logs (format .json)
- 🧹 Clear logs
- 🔄 Mode debug ON/OFF

---

### 📚 Onglet STUDY

**Configuration apprentissage :**

```
Étude automatique:
  [ ✓ ] Activer étude automatique
  [ ] Pause étude
  
Progression:
  Dernier sujet: "Intelligence artificielle"
  Progrès: 65% ████████████░░░
  
Résumé du jour:
  3 sujets étudiés
  12 entrées Wikipedia consultées
  
[Voir synthèse] [Nouveau sujet]
```

---

## 🌐 Paramètres globaux

### Onglet PARAMÈTRES

```yaml
Modes de performance:
  ⦿ Standard
  ◯ Gaming (optimisé FPS)
  ◯ Économie (batterie)

Threading:
  Multithread: [ ✓ ] ON/OFF

Logs:
  Rotation automatique: [ ✓ ]
  Conserver logs: [30] jours
  
Mémoire:
  [Purge mémoire] ⚠️
  [Export mémoire]
```

---

## 🚫 Règles UI

### Ce qui NE doit PAS être accessible

| Élément | Raison |
|---------|--------|
| ❌ Journal intime | Strictement privé |
| ❌ Marks émotionnels internes | Données internes |
| ❌ Paramètres critiques | Hors mode debug |

### Restrictions

- Le journal intime reste **inaccessible**
- Les marks émotionnels **ne sont pas éditables**
- Les paramètres critiques nécessitent **mode debug**

---

## 🎨 Mockup de l'interface

```
┌────────────────────────────────────────────────┐
│  🌙 Kaguya IA                          [_ □ ×] │
├────────────────────────────────────────────────┤
│  💬 Conversation  👤 Profil  ⚙️ Modèles       │
│  ⚡ Actions  🐛 Debug  📚 Study  🌐 Paramètres │
├────────────────────────────────────────────────┤
│                                                │
│  [Contenu de l'onglet actif]                  │
│                                                │
│                                                │
│                                                │
│                                                │
├────────────────────────────────────────────────┤
│  État: 🟢 Actif  |  Mode: Realtime            │
│  Émotion: 😐 Neutral  |  Latence: 320ms       │
└────────────────────────────────────────────────┘
```

---

## 🎯 Checklist UI

### Phase implémentation

- [ ] Design wireframes
- [ ] Onglet Conversation
- [ ] Onglet Profil
- [ ] Onglet Modèles
- [ ] Onglet Actions
- [ ] Onglet Debug
- [ ] Onglet Study
- [ ] Paramètres globaux
- [ ] Sauvegarde préférences
- [ ] Tests utilisabilité

---

<div align="center">

**[← Retour à l'index](README.md)** | **[Debug & Logging →](DEBUG_LOGGING.md)**

</div>
