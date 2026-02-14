# Rapport — Phase 0 : EventBus + Logger Central
Date: 2026-02-14

## Contexte (demande)
Mise en place du socle de code pour démarrer Kaguya IA : bus d’événements central + logging structuré.  
Objectif : découplage strict inter-modules + traçabilité ("bug vs comportement volontaire").

## Fichiers concernés
- Créés :
  - `src/kaguya/core/event_bus.py`
  - `src/kaguya/core/logger.py`
  - `src/kaguya/app.py`
  - `src/kaguya/__init__.py`

## Extrait avant modification
N/A (nouveaux fichiers)

## Modifications effectuées (après)
- EventBus supporte handlers sync/async, abonnement par event name, wildcard "*".
- LoggerManager écrit en JSON lines, séparation par channel, rotation basique par taille.
- app.py permet un test direct en publiant un événement USER_SPOKE et en loggant la chaîne.

## Choix techniques
- Découplage strict via EventBus pour éviter dépendances directes.
- Logs JSON pour filtrage & debug facile (compatible futur viewer UI).
- Rotation simple pour éviter explosion des fichiers logs.
