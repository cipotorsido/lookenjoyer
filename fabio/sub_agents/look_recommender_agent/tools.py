

from typing import Optional, Dict, Union

def search_fashion_items(
    event_type: str,
    style: Optional[str] = None,
    gender: Optional[str] = None,
    body_type: Optional[str] = None
) -> Dict[str, Union[bool, str, list]]:
    """
    Retorna sugestões de peças de roupas populares para o perfil informado.

    Args:
        event_type: Tipo de evento (ex: show, casamento, churrasco)
        style: Estilo pessoal do usuário (casual, ousado, etc.)
        gender: Gênero do usuário
        body_type: Tipo corporal

    Returns:
        Lista simulada de peças coerentes com o contexto
    """
    # Simulação de busca em um banco de dados de moda (exemplo fixo)
    look_items = {
        "show": {
            "casual": ["camiseta estampada", "short jeans", "botinha", "pochete"],
            "ousado": ["cropped neon", "saia vinil", "coturno"]
        },
        "casamento": {
            "discreto": ["vestido midi floral", "sapatilha nude", "brinco pérola"],
            "ousado": ["macacão acetinado", "salto alto", "clutch metalizada"]
        }
    }

    selected = look_items.get(event_type.lower(), {}).get(style.lower() if style else "casual", [])

    return {
        "success": True,
        "items": selected if selected else ["camisa social", "calça jeans", "tênis branco"],
        "source": "FashionDB"
    }

def get_weather_advice(climate: str) -> Dict[str, Union[bool, str]]:
    """
    Fornece sugestões com base no clima previsto.

    Args:
        climate: Clima informado (ex: "frio", "quente", "chuvoso")

    Returns:
        Recomendações de peças ou cuidados
    """
    advice = {
        "frio": "Considere incluir jaqueta, casaco leve ou segunda pele.",
        "quente": "Prefira roupas leves, tecidos respiráveis e cores claras.",
        "chuvoso": "Evite tecidos que absorvem água. Use tênis fechado ou galochas, e leve capa ou guarda-chuva."
    }

    return {
        "success": True,
        "advice": advice.get(climate.lower(), "Clima neutro — sem recomendações especiais.")
    }

def fetch_previous_looks(user_id: str) -> Dict[str, Union[bool, list]]:
    """
    Busca as últimas recomendações de look feitas ao usuário.

    Args:
        user_id: ID do usuário (WhatsApp, por exemplo)

    Returns:
        Lista de sugestões anteriores
    """
    # Simulação de histórico
    fake_history = {
        "user_joao": ["Look casual para show sertanejo com botinha e camisa xadrez", "Look discreto para entrevista com calça bege e camisa social"],
    }

    return {
        "success": True,
        "history": fake_history.get(user_id, [])
    }


    pass