# 🌙 Kaguya IA - Debug & Logging System

> **Version** 1.0 | **Statut** Spécification Technique

---

## 📋 Table des matières

1. [Objectif](#objectif)
2. [Principes généraux](#principes-généraux)
3. [Structure du logger](#structure-du-logger)
4. [Niveaux de log](#niveaux-de-log)
5. [Format standardisé](#format-standardisé)
6. [Logs par module](#logs-obligatoires-par-module)
7. [Distinction bug vs comportement](#distinction-bug-vs-comportement)
8. [Logs performance](#logs-performance)
9. [Checklist d'implémentation](#checklist-dimplémentation)

---

## 🎯 Objectif

Le système de logging est **un pilier fondamental du projet**. Il doit permettre de :

- 🔍 **Comprendre** chaque décision de Kaguya
- 🐛 **Distinguer** bug et comportement volontaire
- 😊 **Tracer** les états émotionnels
- ⚙️ **Tracer** les actions système
- 🎤 **Diagnostiquer** les problèmes audio / LLM
- 📊 **Auditer** les performances (latence, RAM, VRAM)

---

## 📐 Principes généraux

| # | Règle |
|---|-------|
| 1 | Aucun module ne logge librement |
| 2 | Tous les logs passent par le Logger central |
| 3 | Format structuré obligatoire |
| 4 | Chaque log doit inclure timestamp, module, level, event_type et payload |

---

## 🗂️ Structure du logger

### Fichiers de logs

```
logs/
 ├── system.log          # Logs système généraux
 ├── emotion.log         # États émotionnels
 ├── audio.log           # Pipeline audio
 ├── actions.log         # Actions système
 ├── brain.log           # LLM et génération
 ├── memory.log          # Système mémoire
 └── performance.log     # Métriques performance
```

> **Note :** Rotation automatique recommandée.

---

## 🎚️ Niveaux de log

### Niveaux standards

- `DEBUG` - Information de débogage détaillée
- `INFO` - Information générale
- `WARNING` - Avertissement
- `ERROR` - Erreur
- `CRITICAL` - Erreur critique

### Niveaux spécifiques projet

- `DECISION` - Décision comportementale
- `EMOTION_UPDATE` - Mise à jour émotionnelle
- `REFLECTION` - Réflexion interne
- `BASELINE_SHIFT` - Modification baseline
- `AUTONOMOUS_ACTION` - Action autonome

---

## 📄 Format standardisé

### Format recommandé : JSON structuré

```json
{
  "timestamp": "2026-02-15T14:32:10",
  "module": "emotion",
  "level": "EMOTION_UPDATE",
  "event": "irritation_increase",
  "payload": {
    "irritation": 0.72,
    "trust": 0.65,
    "cause": "repeated_direct_order"
  }
}
```

### Avantages

✅ Exploitable en analyse  
✅ Facilement filtrable  
✅ Compatible outils externes  

---

## 📦 Logs obligatoires par module

### 6.1 Emotion

| Event | Description |
|-------|-------------|
| `EMOTION_UPDATE` | Mise à jour état émotionnel |
| `REFLECTION` | Processus de réflexion |
| `BASELINE_SHIFT` | Modification du baseline |
| `MARK_CREATED` | Création d'un mark émotionnel |
| `MARK_RESOLVED` | Résolution d'un mark |

**Exemple :**
```json
{
  "timestamp": "2026-02-15T14:32:10",
  "module": "emotion",
  "level": "EMOTION_UPDATE",
  "event": "irritation_increase",
  "payload": {
    "previous_value": 0.45,
    "new_value": 0.72,
    "cause": "repeated_interruption"
  }
}
```

---

### 6.2 Brain

| Event | Description |
|-------|-------------|
| `GENERATION_START` | Début génération LLM |
| `GENERATION_END` | Fin génération LLM |
| `MODE_SWITCH` | Changement mode (realtime/qualité) |
| `CONTEXT_INJECTION` | Injection contexte |

**Exemple :**
```json
{
  "timestamp": "2026-02-15T14:32:15",
  "module": "brain",
  "level": "INFO",
  "event": "generation_start",
  "payload": {
    "mode": "realtime",
    "context_size": 2048
  }
}
```

---

### 6.3 Audio

| Event | Description |
|-------|-------------|
| `AUDIO_INPUT` | Capture audio |
| `STT_RESULT` | Résultat transcription |
| `TTS_START` | Début synthèse |
| `TTS_STREAM_CHUNK` | Chunk audio généré |
| `TTS_END` | Fin synthèse |
| `INTERRUPTION` | Interruption TTS |

**Exemple :**
```json
{
  "timestamp": "2026-02-15T14:32:20",
  "module": "audio",
  "level": "INFO",
  "event": "stt_result",
  "payload": {
    "text": "Bonjour Kaguya",
    "confidence": 0.95,
    "latency_ms": 320
  }
}
```

---

### 6.4 Actions

| Event | Description |
|-------|-------------|
| `DECISION` | Décision d'action |
| `AUTONOMOUS_ACTION` | Action autonome |
| `ACTION_SUCCESS` | Action réussie |
| `ACTION_FAILURE` | Action échouée |

**Exemple :**
```json
{
  "timestamp": "2026-02-15T14:32:25",
  "module": "actions",
  "level": "DECISION",
  "event": "autonomous_action",
  "payload": {
    "action": "lower_volume",
    "reason": "high_irritation",
    "irritation_level": 0.82
  }
}
```

---

### 6.5 Memory

| Event | Description |
|-------|-------------|
| `MEMORY_WRITE` | Écriture mémoire |
| `MEMORY_READ` | Lecture mémoire |
| `LIFE_EVENT_CREATED` | Événement de vie créé |
| `DECAY_APPLIED` | Décroissance appliquée |

**Exemple :**
```json
{
  "timestamp": "2026-02-15T14:32:30",
  "module": "memory",
  "level": "INFO",
  "event": "life_event_created",
  "payload": {
    "category": "milestone",
    "description": "First successful conversation",
    "emotional_impact": 0.8
  }
}
```

---

### 6.6 Performance

| Event | Description |
|-------|-------------|
| `CPU_USAGE` | Utilisation CPU |
| `RAM_USAGE` | Utilisation RAM |
| `VRAM_USAGE` | Utilisation VRAM |
| `RESPONSE_LATENCY` | Latence réponse totale |
| `STT_LATENCY` | Latence STT |
| `TTS_LATENCY` | Latence TTS |

**Exemple :**
```json
{
  "timestamp": "2026-02-15T14:32:35",
  "module": "performance",
  "level": "INFO",
  "event": "response_metrics",
  "payload": {
    "stt_ms": 320,
    "brain_ms": 1240,
    "tts_ms": 780,
    "total_ms": 2340
  }
}
```

---

## 🐛 Distinction bug vs comportement

### Comportement volontaire

Si Kaguya ignore volontairement :

```json
{
  "level": "DECISION",
  "event": "ignore_user",
  "payload": {
    "reason": "irritation_high",
    "irritation": 0.83,
    "baseline": "tense"
  }
}
```

### Bug système

Si elle plante :

```json
{
  "level": "ERROR",
  "event": "generation_failed",
  "payload": {
    "error_type": "ModelLoadException",
    "stack_trace": "..."
  }
}
```

### Règle importante

Chaque décision atypique doit inclure :
- `reason` - Raison de la décision
- `emotional_state_snapshot` - État émotionnel au moment
- `baseline_snapshot` - État du baseline

---

## 📊 Logs performance

### Métriques obligatoires

Toutes les latences doivent être mesurées :

```json
{
  "event": "response_metrics",
  "payload": {
    "stt_ms": 320,
    "brain_ms": 1240,
    "tts_ms": 780,
    "total_ms": 2340
  }
}
```

### Métriques système

```json
{
  "event": "system_metrics",
  "payload": {
    "cpu_percent": 45.2,
    "ram_mb": 2048,
    "vram_mb": 6144,
    "gpu_utilization": 67.5
  }
}
```

---

## 🖥️ Mode Debug UI

### Fonctionnalités requises

L'UI doit proposer :

- 🔄 **Toggle Debug Mode** - Activer/désactiver mode debug
- 👁️ **Visualisation live** - Affichage temps réel des logs
- 🔍 **Filtrage par module** - Filtres par catégorie
- 💾 **Export .log** - Exportation des logs
- 🧹 **Clear logs** - Nettoyage des logs

---

## 🔒 Sécurité

### Ce que les logs ne doivent JAMAIS contenir :

- ❌ Clés API
- ❌ Données sensibles utilisateur
- ❌ Audio brut persistant

> **Note importante :** Le journal intime ne doit **PAS** être exposé dans les logs.

---

## 🔄 Rotation & Nettoyage

### Configuration

- 📦 **Rotation par taille** - Nouveau fichier si > X Mo
- 🧹 **Suppression automatique** - Logs > X jours
- ⚙️ **Paramétrable** - Configuration dans l'UI

### Exemple configuration

```yaml
log_rotation:
  max_size_mb: 100
  max_age_days: 30
  backup_count: 5
```

---

## 🧪 Tests logging

### Avant toute release

Liste de vérification :

- [ ] ✅ Une ignorance est loggée
- [ ] ✅ Une action autonome est loggée
- [ ] ✅ Chaque module écrit correctement
- [ ] ✅ Rotation automatique fonctionne
- [ ] ✅ Format JSON valide
- [ ] ✅ Timestamps corrects

---

## ✅ Checklist d'implémentation

### Phase 1 – Logger Central
- [ ] Créer `LoggerManager`
- [ ] Format JSON structuré
- [ ] Timestamp ISO standard
- [ ] Séparation fichiers par module

### Phase 2 – Intégration Modules
- [ ] Emotion logs
- [ ] Brain logs
- [ ] Audio logs
- [ ] Actions logs
- [ ] Memory logs

### Phase 3 – Performance Metrics
- [ ] Mesure latence STT
- [ ] Mesure latence Brain
- [ ] Mesure latence TTS
- [ ] Log total response time

### Phase 4 – UI Debug
- [ ] Toggle debug mode
- [ ] Live viewer
- [ ] Export logs
- [ ] Rotation automatique
- [ ] Filtrage par module

---

<div align="center">

**[← Retour à l'index](README.md)** | **[UI Specification →](UI_SPECIFICATION.md)**

</div>
