# 🌙 Kaguya IA - Agent Development Rules

> **Statut** Règles Obligatoires de Développement ⚠️

---

## ⚠️ Avertissement

Ce fichier définit les **règles absolues** pour toute modification du projet Kaguya.

**Violation de ces règles = Risque de corruption du système émotionnel et comportemental.**

---

## 🔒 RÈGLES ABSOLUES

### 1. Architecture

| # | Règle | Raison |
|---|-------|--------|
| 1 | Ne jamais supprimer un module sans justification écrite | Préservation architecture |
| 2 | Ne jamais coupler directement deux modules | Maintenabilité |
| 3 | Toute action autonome doit être loggée | Traçabilité |
| 4 | Aucune émotion basée sur timer fixe | Crédibilité psychologique |
| 5 | Aucun reset brutal du mood baseline | Continuité émotionnelle |

---

### 2. Sécurité & Privacy

| # | Règle | Raison |
|---|-------|--------|
| 6 | Le journal intime est strictement inaccessible | Protection vie privée de l'IA |
| 7 | Les décisions atypiques doivent être traçables | Débogage comportemental |
| 8 | Le nom utilisateur vient exclusivement de l'UI | Sécurité |
| 9 | Répondre à l'utilisateur reste prioritaire | UX fondamentale |
| 10 | Toute nouvelle fonctionnalité doit être documentée | Maintenabilité |

---

## 🐛 PROCESSUS EN CAS D'ERREUR

### Méthodologie obligatoire

```
1. Lire les logs
   └─> Identifier l'événement déclencheur
   
2. Identifier le module responsable
   └─> Vérifier les événements émis
   
3. Corriger sans casser l'architecture
   └─> Respecter le découplage des modules
   
4. Tester l'interaction émotionnelle
   └─> Vérifier baseline, marks, réflexion
   
5. Documenter la modification
   └─> Mettre à jour la documentation concernée
```

---

## ❌ INTERDICTIONS STRICTES

### Actions interdites

| Interdit | Raison | Alternative |
|----------|--------|-------------|
| ❌ Accès système critique | Sécurité | Whitelist + validation |
| ❌ Modification non sécurisée | Stabilité | Wrapper sécurisé |
| ❌ Dépendance directe inter-modules | Couplage | EventBus |
| ❌ Accès direct au stockage mémoire | Intégrité | MemoryManager |

---

### Exemples de violations

#### ❌ MAUVAIS

```python
# Violation règle #2 (couplage direct)
from emotion.emotion_engine import EmotionEngine
emotion = EmotionEngine()
emotion.set_irritation(0.8)  # ❌ Appel direct
```

#### ✅ BON

```python
# Respect architecture (EventBus)
from core.event_bus import EventBus
EventBus.emit("USER_IRRITATING_ACTION", {
    "reason": "repeated_interruption"
})
```

---

#### ❌ MAUVAIS

```python
# Violation règle #4 (timer fixe)
def update_emotion():
    every_hour():  # ❌ Timer fixe
        irritation -= 0.1
```

#### ✅ BON

```python
# Respect architecture (réflexion contextuelle)
def internal_reflection(trigger_event):
    if should_reflect(trigger_event):  # ✅ Contextuel
        adjust_emotions_based_on_context()
```

---

## 🎯 PRIORITÉS DE DÉVELOPPEMENT

### Ordre de priorité

```
1. Stabilité      > Fonctionnalités
2. Cohérence      > Rapidité
3. Architecture   > Patch rapide
4. Documentation  > Code quick & dirty
```

### Explication

| Priorité | Pourquoi |
|----------|----------|
| **Stabilité** | Un système stable avec moins de features vaut mieux qu'un système riche mais instable |
| **Cohérence** | La crédibilité psychologique repose sur la cohérence comportementale |
| **Architecture** | Une architecture propre facilite l'évolution future |
| **Documentation** | Code non documenté = dette technique future |

---

## 📝 DOCUMENTATION OBLIGATOIRE

### Avant d'ajouter une fonctionnalité

- [ ] Vérifier compatibilité architecture existante
- [ ] Identifier modules impactés
- [ ] Documenter les changements
- [ ] Mettre à jour la ROADMAP si nécessaire
- [ ] Ajouter tests si applicable

---

## 🔍 CHECKLIST PRE-COMMIT

Avant tout commit, vérifier :

### Fonctionnel
- [ ] Le code compile
- [ ] Les tests passent
- [ ] Aucune régression détectée

### Architecture
- [ ] Aucun couplage direct ajouté
- [ ] EventBus utilisé pour communication
- [ ] Logging approprié ajouté

### Documentation
- [ ] Commentaires code ajoutés
- [ ] Documentation technique mise à jour
- [ ] CHANGELOG mis à jour

---

## 🚨 EN CAS D'URGENCE

### Bug critique en production

```
1. Isoler le module défaillant
2. Consulter les logs (CRITICAL level)
3. Rollback si nécessaire
4. Fix avec tests
5. Documentation post-mortem
```

---

## 📚 RESSOURCES

### Documents de référence

| Document | Utilisation |
|----------|-------------|
| `ARCHITECTURE.md` | Structure globale |
| `EMOTION_ENGINE.md` | Système émotionnel |
| `MEMORY_SYSTEM.md` | Gestion mémoire |
| `ROADMAP.md` | Plan développement |

---

## ⚖️ PRINCIPE FONDAMENTAL

> **"Kaguya doit se comporter comme une entité psychologiquement cohérente,  
> pas comme un ensemble de scripts qui s'exécutent."**

Toute modification doit servir cet objectif.

---

## ✅ Acceptation des règles

En contribuant au projet Kaguya, vous acceptez :

- ✅ De respecter ces règles absolues
- ✅ De documenter vos modifications
- ✅ De prioriser stabilité sur rapidité
- ✅ De maintenir la cohérence psychologique

---

<div align="center">

**[← Retour à l'index](README.md)**

**Dernière mise à jour : 2026-02-15**

</div>
