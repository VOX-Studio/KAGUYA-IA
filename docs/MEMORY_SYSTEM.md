# 🌙 Kaguya IA - Memory System

> **Version** 1.0 | **Statut** Spécification Technique Fondamentale ⭐

---

## 📋 Table des matières

1. [Objectif](#objectif)
2. [Architecture globale](#architecture-globale)
3. [Types de mémoire](#types-de-mémoire)
4. [Priorisation](#priorisation)
5. [Décroissance](#décroissance-decay-engine)
6. [Intégration avec Emotion Engine](#intégration-avec-emotion-engine)
7. [Persistence](#persistence)
8. [Checklist d'implémentation](#checklist-dimplémentation)

---

## 🎯 Objectif

Le **Memory System** permet à Kaguya de maintenir une continuité cognitive et relationnelle.

### Fonctionnalités

- 💭 **Se souvenir** du contexte immédiat
- 💾 **Stocker** des informations importantes sur l'utilisateur
- 📚 **Construire** une mémoire long terme
- 📖 **Conserver** son histoire ("enfance")
- 📝 **Résumer** ses apprentissages
- 📈 **Alimenter** le baseline émotionnel
- 🔄 **Réduire** les recherches répétitives

### Caractéristiques

- ✅ **Structurée** - Organisation claire
- ✅ **Priorisée** - Importance relative
- ✅ **Décroissante** - Oubli progressif
- ✅ **Persistante** - Sauvegarde sur disque
- ✅ **Interconnectée** - Avec l'Emotion Engine

---

## 🏗️ Architecture globale

```
memory/
 ├── short_term_memory.py    # Mémoire court terme
 ├── long_term_memory.py     # Mémoire long terme
 ├── knowledge_memory.py     # Mémoire de connaissances
 ├── life_events.py          # Événements de vie
 ├── memory_prioritizer.py   # Système de priorisation
 ├── decay_engine.py         # Moteur de décroissance
 ├── memory_storage.py       # Stockage persistant
 └── memory_manager.py       # Gestionnaire principal
```

---

## 💾 Types de mémoire

### 3.1 Short-Term Memory (STM)

**Rôle :**
- 💬 Maintenir le contexte conversationnel actif
- 🔄 Conserver les 5-20 derniers échanges
- 🎯 Stocker les intentions en cours

**Caractéristiques :**
- ⚡ Volatile
- 🔄 Réinitialisée à la fermeture
- 📝 Non persistante

**Utilisée par :**
- 🧠 Brain
- 😊 Emotion Engine

---

### 3.2 Long-Term Memory (LTM)

**Rôle :**
- 👤 Informations importantes sur l'utilisateur
- ⭐ Préférences
- 🔄 Habitudes
- 🎭 Traits de personnalité détectés
- ⚔️ Conflits passés
- ✨ Moments marquants

**Persistance :** Sur disque

**Structure recommandée :**

```python
class MemoryEntry:
    id: str
    category: str                # preference, habit, conflict, milestone
    importance_score: float      # 0.0 - 1.0
    emotional_weight: float      # 0.0 - 1.0
    created_at: datetime
    last_accessed: datetime
    content: dict
    tags: list[str]
```

---

### 3.3 Knowledge Memory

**Rôle :**
- 📚 Stocker résumés Wikipedia
- 🔄 Éviter recherches répétées
- 📝 Synthétiser apprentissages

**Structure :**

```python
class KnowledgeEntry:
    topic: str
    summary: str
    source: str
    last_verified: datetime
    confidence_score: float     # 0.0 - 1.0
```

> **Note :** Peut être réactualisée périodiquement (tous les X mois).

---

### 3.4 Life Events (Mémoire d'Enfance)

**Rôle :**
- 🧪 Enregistrer phases de test
- 🐛 Bugs marquants
- 🎯 Changements majeurs
- 📈 Évolutions techniques

**Structure :**

```python
class LifeEvent:
    category: str               # test_phase, milestone, failure, success
    description: str
    emotional_impact: float     # -1.0 à 1.0
    timestamp: datetime
```

**Alimente :**
- 📈 Baseline émotionnel
- 📔 Journal intime
- 📖 Narration future

---

## 📊 Priorisation

### Score de priorisation

Chaque `MemoryEntry` possède :

```python
{
    "importance_score": float,      # Importance rationnelle (0-1)
    "emotional_weight": float,      # Poids émotionnel (0-1)
    "usage_frequency": int          # Nombre d'accès
}
```

### Fonction de priorisation

```python
def memory_prioritizer():
    # Augmenter score si réutilisé
    if frequently_accessed:
        importance_score += 0.1
    
    # Augmenter score si émotionnellement chargé
    if emotional_weight > 0.7:
        importance_score += 0.15
    
    # Diminuer score si inutilisé
    if days_since_access > 30:
        importance_score -= 0.05
```

---

## 📉 Décroissance (Decay Engine)

### Objectif

**Éviter l'accumulation infinie de données**

### Règles

| Type de mémoire | Règle de décroissance |
|----------------|----------------------|
| **Peu utilisées** | ↘️ Importance diminue |
| **Émotionnelles** | ↘️ Décroissance plus lente |
| **LifeEvents** | ✅ Pas de décroissance auto |
| **Connaissances** | ⚠️ Marquées "needs_update" |

> **Important :** Décroissance progressive, jamais suppression brutale sans archivage.

---

## 🔗 Intégration avec Emotion Engine

### Le Memory System :

- ✅ Crée `EmotionalMarks` si événement important
- ✅ Fournit contexte pour réflexion
- ✅ Influence baseline via poids émotionnel
- ✅ Stocke résolution de conflits

### L'Emotion Engine :

- ❌ Ne modifie **pas** directement la mémoire
- ✅ Passe par `MemoryManager`

---

## 🔐 Accès aux données

### Contrôle d'accès

Tous les accès passent par :

```python
memory_manager.py
```

### Interdictions

- ❌ Aucun module n'accède directement aux fichiers
- ❌ Pas d'écriture sauvage

---

## 💾 Persistence

### Stockage recommandé

**Options :**
- 📄 JSON structuré
- 🗄️ SQLite local

**Doit permettre :**
- ⚡ Lecture rapide
- 🔍 Filtrage par tags
- 📊 Tri par importance
- 💾 Sauvegarde incrémentale

---

## 📝 Résumé automatique

### Fonction

```python
def periodic_memory_summarization():
    """
    - Compresser souvenirs anciens
    - Fusionner entrées similaires
    - Maintenir cohérence narrative
    """
```

### Déclenchement

- 📅 Périodique (hebdomadaire/mensuel)
- 📦 Quand stockage > seuil
- 🎯 Sur demande utilisateur

---

## 👤 Mémoire utilisateur (Profil)

### Profil stocké séparément

```python
class UserProfile:
    display_name: str
    pronoms: str = None        # Optionnel
    surnoms_autorisés: list
    date_creation: datetime
    préférences_stables: dict
```

> **Règle stricte :** Le nom affiché est défini via UI. Jamais déduit automatiquement.

---

## 🔒 Sécurité

### Mesures de protection

- ❌ Aucun stockage audio brut permanent
- ❌ Pas de données sensibles inutiles
- ✅ Option purge mémoire via UI
- ✅ Journal intime séparé du LTM

---

## 📋 Logs mémoire

### Logs obligatoires

| Log | Description |
|-----|-------------|
| `MEMORY_WRITE` | Écriture d'une entrée |
| `MEMORY_READ` | Lecture d'une entrée |
| `MEMORY_DECAY` | Décroissance appliquée |
| `LIFE_EVENT_CREATED` | Événement de vie créé |
| `KNOWLEDGE_UPDATED` | Connaissance mise à jour |

---

## ✅ Checklist d'implémentation

### Phase 1 – Structure
- [ ] Créer dossier `memory/`
- [ ] Créer `MemoryManager`
- [ ] Créer `ShortTermMemory`
- [ ] Créer `LongTermMemory`
- [ ] Créer `KnowledgeMemory`
- [ ] Créer `LifeEvents`

### Phase 2 – Priorisation
- [ ] Implémenter `importance_score`
- [ ] Implémenter `emotional_weight`
- [ ] Implémenter usage tracking

### Phase 3 – Décroissance
- [ ] Implémenter `DecayEngine`
- [ ] Implémenter archivage
- [ ] Empêcher suppression brutale

### Phase 4 – Résumé
- [ ] Implémenter `periodic_memory_summarization`
- [ ] Fusion entrées similaires

### Phase 5 – Intégration Emotion
- [ ] Liaison `EmotionalMark`
- [ ] Influence baseline
- [ ] Stockage résolution conflits

### Phase 6 – Persistence
- [ ] Choix stockage (JSON / SQLite)
- [ ] Sauvegarde automatique
- [ ] Chargement au démarrage

### Phase 7 – UI
- [ ] Visualisation mémoire utilisateur
- [ ] Option purge
- [ ] Affichage importance

---

<div align="center">

**[← Retour à l'index](README.md)** | **[Action System →](ACTION_SYSTEM.md)**

</div>
