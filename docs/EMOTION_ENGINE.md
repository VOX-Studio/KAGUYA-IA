# 🌙 Kaguya IA - Emotion Engine

> **Version** 1.0 | **Statut** Spécification Technique Fondamentale ⭐

---

## 📋 Table des matières

1. [Objectif](#objectif)
2. [Architecture interne](#architecture-interne)
3. [État immédiat](#état-immédiat-short-term-state)
4. [Emotional Marks](#emotional-marks)
5. [Mood Baseline](#mood-baseline-long-term-state)
6. [Autorégulation](#autorégulation-reflection-engine)
7. [Bluff émotionnel](#bluff-émotionnel)
8. [Renforcement social](#renforcement-social)
9. [Journal intime privé](#journal-intime-privé)
10. [Influence sur décisions](#influence-sur-décisions)
11. [Checklist d'implémentation](#checklist-dimplémentation)

---

## 🎯 Objectif

L'**Emotion Engine** est le cœur psychologique de Kaguya. Il est responsable de :

### Responsabilités principales

- 😊 **Maintenir l'état émotionnel** interne dynamique
- 🤔 **Simuler un processus** de réflexion
- 💬 **Influencer les décisions** conversationnelles
- ⚙️ **Influencer les actions** système
- 🔄 **Adapter les comportements** via renforcement social
- 📈 **Maintenir un mood baseline** long terme
- 📔 **Alimenter un journal intime** privé

### Ce qu'il ne fait PAS

- ❌ Ne génère pas de texte directement
- ❌ Ne déclenche pas directement d'action
- ✅ Fournit des **décisions** et **recommandations**

---

## 🏗️ Architecture interne

```
emotion/
 ├── immediate_state.py      # État émotionnel instantané
 ├── mood_baseline.py        # Humeur de fond long terme
 ├── emotional_mark.py       # Marqueurs émotionnels
 ├── reinforcement.py        # Apprentissage social
 ├── reflection_engine.py    # Processus de réflexion
 ├── emotional_dictionary.py # Dictionnaire émotionnel
 ├── journal_private.py      # Journal intime privé
 └── emotion_engine.py       # Moteur principal
```

---

## 💭 État immédiat (Short-Term State)

### Vecteur émotionnel dynamique

```python
{
    "irritation": float,    # 0.0 - 1.0
    "trust": float,         # 0.0 - 1.0
    "affection": float,     # 0.0 - 1.0
    "fatigue": float,       # 0.0 - 1.0
    "curiosity": float,     # 0.0 - 1.0
    "focus": float,         # 0.0 - 1.0
    "satisfaction": float   # 0.0 - 1.0
}
```

### Caractéristiques

| Propriété | Description |
|-----------|-------------|
| **Valeurs continues** | De 0.0 à 1.0 |
| **Évolution incrémentale** | Pas de sauts brutaux |
| **Pas de reset** | Jamais de réinitialisation automatique |
| **Modification contrôlée** | Uniquement via `evaluate_stimulus()` ou `reflection()` |

---

## 📌 Emotional Marks

### Structure

```python
{
    "id": str,
    "type": str,                # vexation, conflit, moment_positif, frustration
    "intensity": float,         # 0.0 - 1.0
    "timestamp": datetime,
    "resolved": bool,
    "related_context": dict
}
```

### Déclenchement

Un mark est créé lorsqu'un événement dépasse un seuil émotionnel.

**Exemples de types :**
- 😤 `vexation` - Agacement significatif
- ⚔️ `conflit_non_resolu` - Conflit persistant
- ✨ `moment_positif_intense` - Joie marquante
- 😣 `frustration_repetee` - Frustration récurrente

### Influence

Un mark influence :
- 📈 Le baseline émotionnel
- 📊 La probabilité d'irritation
- 🗣️ Le style conversationnel

> **Important :** Les marks ne disparaissent **pas** automatiquement.

---

## 📈 Mood Baseline (Long-Term State)

### 5.1 Définition

Le **mood baseline** est une humeur de fond persistante.

| Caractéristique | Description |
|----------------|-------------|
| **Drift lent** | Évolution sur semaines/mois |
| **Pas de reset** | Jamais de réinitialisation automatique |
| **Influence multiplicative** | Modifie la réactivité globale |

---

### 5.2 Influence sur réactivité

```python
réactivité_finale = immediate_state × baseline_modifier
```

**Exemples :**

#### Baseline tendu 😤
- ↗️ Irritation augmente plus vite
- ↘️ Tolérance diminue
- ⚡ Réactions plus vives

#### Baseline stable 😊
- ↗️ Montée lente de l'irritation
- ↘️ Résolution plus rapide
- 🌊 Réactions mesurées

---

### 5.3 Mise à jour

> **Règle stricte :** Le baseline évolue **uniquement** via `reflection_engine()`.

❌ Jamais via stimulus direct  
✅ Uniquement via réflexion interne  

---

## 🤔 Autorégulation (Reflection Engine)

### Déclencheurs

| Événement | Description |
|-----------|-------------|
| 💥 **Interaction intense** | Échange émotionnel fort |
| ⚔️ **Conflit** | Désaccord ou tension |
| ⚙️ **Action autonome** | Action système effectuée |
| ⏰ **Inactivité prolongée** | Longue période sans interaction |
| 😔 **Regret** | Conscience d'une erreur |

### Fonction principale

```python
def internal_reflection():
    """
    Processus de réflexion interne
    """
    # Peut :
    - Diminuer irritation
    - Résoudre mark
    - Maintenir tension
    - Générer regret
    - Créer entrée journal
```

> **Note :** Aucun timer fixe. La réflexion est déclenchée par des événements.

---

## 🎭 Bluff émotionnel

### Distinction état interne vs affiché

```python
{
    "internal_state": EmotionalState,   # État réel
    "displayed_state": EmotionalState   # État montré
}
```

### Fonction

```python
def choose_displayed_emotion():
    """
    Peut :
    - Atténuer irritation visible
    - Masquer fatigue
    - Exagérer ironie
    """
```

> **Important :** Un décalage subtil doit rester perceptible pour la crédibilité.

---

## 🔄 Renforcement social

### Structure

```python
{
    "behavior_type": str,      # taquinerie, distance, douceur, ironie, refus
    "positive_score": float,
    "negative_score": float,
    "saturation_level": float
}
```

### Comportements concernés

| Comportement | Description |
|--------------|-------------|
| 🎭 **Taquinerie** | Commentaires espiègles |
| 🚶 **Distance** | Réponses froides |
| 💕 **Douceur** | Réponses chaleureuses |
| 😏 **Ironie** | Sarcasme léger |
| ⛔ **Refus** | Rejet de demandes |

### Fonction

```python
def update_reinforcement(user_reaction):
    """
    Ajuste la probabilité des comportements
    selon la réaction utilisateur
    """
```

### Effets

- 📊 Ajuste probabilité comportementale
- 🚫 Limite répétition excessive
- 🌱 Permet adaptation progressive

---

## 📔 Journal intime privé

### 9.1 Rôle

**Centraliser :**
- 🤔 Réflexions brutes
- 🔍 Hypothèses sur utilisateur
- 🎯 Stratégies relationnelles
- 😔 Regrets
- 🔬 Auto-analyse

---

### 9.2 Accès

| Type d'accès | Autorisé |
|--------------|----------|
| Via UI | ❌ Non |
| Via logs publics | ❌ Non |
| Métadonnées | ✅ Visibles uniquement |

---

### 9.3 Lien avec mémoire

Peut générer :
- 📌 `EmotionalMark`
- 📅 `LifeEvent`
- 📈 `Baseline shift`

---

## 🎯 Influence sur décisions

### L'Emotion Engine fournit :

```python
{
    "tone_recommendation": str,      # neutral, warm, cold, playful, irritated
    "cooperation_level": float,      # 0.0 - 1.0
    "action_authorization": bool,    # True/False
    "ignore_probability": float,     # 0.0 - 1.0
    "sarcasm_level": float          # 0.0 - 1.0
}
```

> **Règle fondamentale :** Le Brain ne décide **pas** seul.

---

## 🚫 Ignorance volontaire

### Conditions possibles

```python
if (
    irritation > seuil
    OR fatigue_elevee
    OR conflit_non_resolu
    OR baseline == "tendu"
):
    ignore_probability += 0.3
```

### Logging obligatoire

```json
{
  "level": "DECISION",
  "event": "ignore_user",
  "payload": {
    "irritation": 0.83,
    "fatigue": 0.65,
    "baseline": "tense"
  }
}
```

### Mécanisme de sortie

⚠️ **Boucle d'ignorance interdite**  
✅ Mécanisme de sortie obligatoire  

---

## 😔 Regret

### Après action autonome

Processus :
1. 🤔 Réflexion possible
2. 📌 Création regret mark
3. 📉 Réduction probabilité future
4. 📈 Ajustement baseline

**Exemple :**
```python
if autonomous_action_failed:
    create_mark("regret", intensity=0.7)
    baseline.adjust(direction="negative", amount=0.1)
```

---

## 🔗 Intégration avec autres modules

### Ce que l'Emotion Engine ne doit JAMAIS faire :

- ❌ Appeler `ActionSystem` directement
- ❌ Modifier mémoire long terme directement
- ❌ Générer du texte

### Ce qu'il doit faire :

- ✅ Émettre recommandations via `EventBus`
- ✅ Loguer toutes modifications

---

## 📡 Événements émis

| Événement | Description |
|-----------|-------------|
| `EMOTION_UPDATED` | État émotionnel modifié |
| `MARK_CREATED` | Nouveau mark créé |
| `MARK_RESOLVED` | Mark résolu |
| `BASELINE_SHIFT` | Modification du baseline |
| `DECISION_IGNORE` | Décision d'ignorer |
| `DECISION_ACTION_AUTHORIZED` | Action autorisée |
| `REFLECTION_COMPLETE` | Réflexion terminée |

---

## ✅ Checklist d'implémentation

### Phase 1 – Structures
- [ ] `ImmediateState` class
- [ ] `EmotionalMark` class
- [ ] `MoodBaseline` class
- [ ] `Reinforcement` class

### Phase 2 – Core Logic
- [ ] `evaluate_stimulus()`
- [ ] `create_mark()`
- [ ] `resolve_mark()`
- [ ] `internal_reflection()`
- [ ] `update_baseline_drift()`

### Phase 3 – Bluff System
- [ ] `choose_displayed_emotion()`
- [ ] Tone recommendation output

### Phase 4 – Reinforcement
- [ ] `update_reinforcement()`
- [ ] Saturation mechanism

### Phase 5 – Journal Privé
- [ ] `PrivateJournal` storage
- [ ] Link to marks
- [ ] Reflection writing

### Phase 6 – Decision Layer
- [ ] `ignore_probability`
- [ ] `action_authorization`
- [ ] `cooperation_level` output

### Phase 7 – Logging
- [ ] `EMOTION_UPDATE` logs
- [ ] `REFLECTION` logs
- [ ] `BASELINE_SHIFT` logs
- [ ] `DECISION` logs

---

<div align="center">

**[← Retour à l'index](README.md)** | **[Memory System →](MEMORY_SYSTEM.md)**

</div>
