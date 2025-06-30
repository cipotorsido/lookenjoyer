from typing import Optional, Dict, Union

def register_event_context(
    user_id: str,
    event_type: str,
    location: str,
    music_style: str,
    time_of_day: str,
    climate: str,
    formality: Optional[str] = None,
    specific_requirements: Optional[str] = None
) -> Dict[str, Union[bool, str]]:
    """
    Registra o contexto do evento informado pelo usuário para uso posterior na recomendação de roupas.

    Args:
        user_id: Identificador único do usuário
        event_type: Tipo de evento
        location: Tipo de ambiente físico
        music_style: Estilo musical predominante
        time_of_day: Horário do evento
        climate: Clima estimado
        formality: Grau de formalidade (opcional)
        specific_requirements: Regras ou exigências específicas (opcional)

    Returns:
        Confirmação de sucesso ou mensagem de erro
    """
    required_fields = [event_type, location, music_style, time_of_day, climate]
    if not all(required_fields):
        return {
            "success": False,
            "error": "Todos os campos obrigatórios do evento devem estar preenchidos."
        }

    # Simulação de persistência
    print(f"Registrando evento do usuário {user_id}...")
    print(f"{event_type=}, {location=}, {music_style=}, {time_of_day=}, {climate=}, {formality=}, {specific_requirements=}")

    return {
        "success": True,
        "message": "Contexto do evento registrado com sucesso.",
        "event_id": f"evt_{user_id}"
    }

pass