"""
ImmediateState représente l'état émotionnel court terme.

Responsabilités :
- Stocker les axes émotionnels
- Permettre des mises à jour progressives
- Fournir un snapshot exploitable pour logs

Impacte :
- EmotionEngine
- Logger
- Brain (injection contexte futur)
"""

from dataclasses import dataclass, asdict


@dataclass
class ImmediateState:
    irritation: float = 0.0
    trust: float = 0.5
    affection: float = 0.5
    fatigue: float = 0.0
    curiosity: float = 0.5
    focus: float = 0.5
    satisfaction: float = 0.5

    def clamp(self) -> None:
        """
        Empêche toute valeur de sortir de l'intervalle [0.0, 1.0]
        """
        for field in self.__dataclass_fields__:
            value = getattr(self, field)
            setattr(self, field, max(0.0, min(1.0, value)))

    def snapshot(self) -> dict:
        """
        Retourne un dictionnaire représentant l'état actuel.
        """
        return asdict(self)
