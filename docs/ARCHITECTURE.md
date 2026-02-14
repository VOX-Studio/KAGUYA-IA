# 🌙 Kaguya IA - Architecture Technique Globale

> **Version** 1.0 | **Statut** Spécification Fondamentale

---

## 📋 Table des matières

1. [Objectif](#objectif)
2. [Principes d'architecture](#principes-darchitecture)
3. [Modules principaux](#modules-principaux)
4. [Bus d'événements](#bus-dévénements)
5. [Multithreading](#multithreading)
6. [Système de priorités](#système-de-priorités)
7. [Gestion des ressources](#gestion-des-ressources)
8. [Checklist d'implémentation](#checklist-dimplémentation)

---

## 🎯 Objectif

Ce document définit la structure technique complète du projet Kaguya, incluant :

- 📦 **Les modules** et leurs responsabilités
- 🔄 **Les flux de données** entre composants
- ⚡ **Le multitâche** et la gestion des threads
- 🎚️ **Les priorités d'exécution**
- 💾 **La gestion des ressources** (RAM/VRAM)
- 🔌 **Les contraintes de découplage**

---

## 🏗️ Principes d'architecture

| # | Principe | Description |
|---|----------|-------------|
| 1 | **Modularité stricte** | Chaque module a une responsabilité unique |
| 2 | **Communication par événements** | Utilisation d'un bus d'événements central |
| 3 | **Découplage** | Aucun couplage direct inter-modules |
| 4 | **Stabilité** | Priorité à la fiabilité sur la performance |
| 5 | **Traçabilité** | Logs systématiques de toutes les opérations |
| 6 | **Interruptibilité** | Possibilité d'interruption des tâches longues |
| 7 | **Optimisation** | Gestion efficace de la RAM et VRAM |

---

## 📦 Modules principaux

### 3.1 brain/

**Responsabilités :**
- 🤖 Interface avec le modèle LLM
- 💬 Gestion du contexte conversationnel
- 💉 Injection de l'état émotionnel
- ⚡ Gestion double mode (realtime / qualité)

**Ne doit PAS :**
- ❌ Gérer les émotions directement
- ❌ Gérer l'audio directement

---

### 3.2 emotion/

**Responsabilités :**
- 😊 `ImmediateState` - État émotionnel instantané
- 📌 `EmotionalMarks` - Marqueurs émotionnels persistants
- 📈 `MoodBaseline` - Humeur de fond long terme
- 🤔 `Reflection` - Processus de réflexion interne
- 🔄 `Reinforcement` - Apprentissage social
- 🎭 `Bluff state` - Gestion de l'affichage émotionnel

**Fournit :**
- 🎨 Tonalité recommandée
- 🤝 Niveau de coopération
- ✅ Autorisation d'actions

---

### 3.3 memory/

**Responsabilités :**
- 💭 Mémoire court terme (contexte actif)
- 💾 Mémoire long terme (persistante)
- 📅 `LifeEvents` (histoire personnelle)
- 📚 Résumés de connaissances
- 📉 Priorisation et décroissance

---

### 3.4 audio/

**Responsabilités :**
- 🎤 STT continu (Speech-To-Text)
- 🔊 TTS (Text-To-Speech)
- 📦 Gestion des buffers audio
- ⚡ Optimisation de la latence
- 👂 Détection de parole active (VAD)

---

### 3.5 actions/

**Responsabilités :**
- 🔊 Contrôle du volume système
- 🎵 Gestion de la musique
- 📱 Contrôle des applications
- 💬 Intégration Discord
- ⚙️ Exécution des commandes internes

> **Note :** Toutes les actions doivent passer par ce module.

---

### 3.6 presence/

**Responsabilités :**
- 📷 Webcam (optionnel)
- 🖥️ Partage d'écran
- 👁️ Détection de présence
- 🎯 Détection de focus

---

### 3.7 study/

**Responsabilités :**
- 📖 Recherche Wikipedia
- 📝 Génération de résumés
- 🧠 Apprentissage passif
- ⏸️ Tâche secondaire interrompable

---

### 3.8 scheduler/

**Responsabilités :**
- ⏰ Gestion des rappels
- 🔄 Retour différé
- 🎚️ Gestion des priorités de tâches

---

### 3.9 vtuber/

**Responsabilités :**
- 🎭 États d'animation
- 🔗 Synchronisation émotionnelle
- 👄 Lip-sync
- 🎨 Mouvement procédural

> **Note :** Dernier module à implémenter.

---

### 3.10 ui/

**Responsabilités :**
- 🖥️ Interface utilisateur
- ⚙️ Paramètres des modèles
- 👤 Profil utilisateur
- 🐛 Outils de débogage
- 🔀 Activation du multitâche

---

## 🔌 Bus d'événements

### Principe

Tous les modules communiquent via un **EventBus central**.

**Aucun module n'appelle un autre directement.**

### Événements standards

| Événement | Description |
|-----------|-------------|
| `USER_SPOKE` | L'utilisateur a parlé |
| `EMOTION_UPDATED` | État émotionnel modifié |
| `DECISION_MADE` | Décision prise par le système |
| `ACTION_TRIGGERED` | Action système déclenchée |
| `REFLECTION_COMPLETE` | Réflexion interne terminée |
| `MEMORY_UPDATED` | Mémoire modifiée |

---

## 🧵 Multithreading

### Threads recommandés

```
Thread 1 : STT continu (écoute permanente)
Thread 2 : Brain génération (LLM)
Thread 3 : Emotion engine (calculs émotionnels)
Thread 4 : Actions système (exécution)
Thread 5 : Study background (apprentissage)
Thread 6 : Logging (journalisation)
```

> **Note :** Le multitâche avancé est optionnel et configurable via l'UI.

---

## 🎚️ Système de priorités

### Ordre de priorité absolue

```
1️⃣ Réponse utilisateur (priorité maximale)
2️⃣ STT (écoute continue)
3️⃣ Emotion update (calcul émotionnel)
4️⃣ Actions en cours
5️⃣ Study (apprentissage passif)
6️⃣ VTuber (animation)
```

---

## 💾 Gestion des ressources

### Objectifs

- 🎮 **Minimiser l'usage RAM** en mode gaming
- 🖥️ **Limiter l'usage VRAM** du LLM
- ⏸️ **Suspension automatique** du Study si charge élevée
- ⚡ **TTS streaming** pour réduire la latence

### Stratégies d'optimisation

| Contexte | Optimisation |
|----------|--------------|
| Mode Gaming | Suspension Study + réduction qualité STT |
| Charge CPU élevée | Pause automatique tâches secondaires |
| VRAM limitée | Réduction du contexte LLM |

---

## ⏸️ Interruption des tâches

### Module Study

Doit être :
- ✅ **Interrompable** (arrêt immédiat possible)
- ✅ **Reprisable** (continuation depuis le dernier point)
- ✅ **Checkpointable** (sauvegarde de l'état)

### Brain mode qualité

Doit pouvoir être interrompu par une nouvelle interaction utilisateur.

---

## 🚫 Séparation stricte

### Ce que l'Emotion Engine ne doit JAMAIS faire :

- ❌ Générer du texte directement
- ❌ Exécuter des actions système directement

### Ce que le Brain ne doit JAMAIS faire :

- ❌ Modifier le baseline émotionnel
- ❌ Créer des marks émotionnels directement

### Règle générale

**Les actions doivent passer par validation émotionnelle.**

---

## ✅ Checklist d'implémentation

### Phase 1 – Structure
- [ ] Créer l'arborescence complète
- [ ] Créer `EventBus` central
- [ ] Créer logger central

### Phase 2 – Modules vides
- [ ] `brain/`
- [ ] `emotion/`
- [ ] `memory/`
- [ ] `audio/`
- [ ] `actions/`
- [ ] `presence/`
- [ ] `study/`
- [ ] `scheduler/`
- [ ] `vtuber/`
- [ ] `ui/`

### Phase 3 – Communication
- [ ] Implémenter événements standards
- [ ] Tester propagation des événements

### Phase 4 – Multithreading
- [ ] Implémenter threads séparés
- [ ] Tester interruption Study
- [ ] Tester priorité réponse

### Phase 5 – Optimisation
- [ ] Profil RAM
- [ ] Profil VRAM
- [ ] Test multitâche ON/OFF

---

## 📊 Diagramme d'architecture

```
┌─────────────────────────────────────────────┐
│           EventBus Central                  │
└─────────────────────────────────────────────┘
          │         │         │         │
    ┌─────┴──┐ ┌───┴───┐ ┌──┴────┐ ┌──┴────┐
    │ Brain  │ │Emotion│ │Memory │ │ Audio │
    └────────┘ └───────┘ └───────┘ └───────┘
          │         │         │         │
    ┌─────┴──┐ ┌───┴───┐ ┌──┴────┐ ┌──┴────┐
    │Actions │ │Study  │ │Presence│ │VTuber│
    └────────┘ └───────┘ └────────┘ └───────┘
```

---

<div align="center">

**[← Retour à l'index](README.md)** | **[Emotion Engine →](EMOTION_ENGINE.md)**

</div>
