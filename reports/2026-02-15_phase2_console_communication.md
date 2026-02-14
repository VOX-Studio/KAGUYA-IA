# Rapport – Phase 2 : Communication Console
Date : 2026-02-15

---

## Contexte

Objectif : permettre communication directe avec Kaguya avant intégration LLM ou audio.

---

## Fichiers Créés

- src/kaguya/brain/__init__.py
- src/kaguya/brain/brain_stub.py

## Fichier Modifié

- src/kaguya/app.py

---

## Fonctionnement

USER_INPUT → USER_SPOKE → EmotionEngine update → BrainStub response → KAGUYA_RESPONSE → affichage console

---

## Choix Techniques

- BrainStub temporaire
- Influence émotionnelle minimale
- Boucle console synchrone
- Aucun couplage direct entre modules
- EventBus central respecté

---

## Validation

Commande :

python -m kaguya.app

Attendu :
- Kaguya répond en console
- Irritation augmente si texte contient "!"
- Logs créés correctement
