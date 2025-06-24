from typing import Optional, Dict, Union

def register_user_profile(
    name: str,
    age: int,
    gender: str,
    body_type: str,
    style_preference: str,
    notes: Optional[str] = None
) -> Dict[str, Union[bool, str]]:
    """
    Registra o perfil do usuário para fins de recomendação de roupas.

    Args:
        name: Nome como o usuário gostaria de ser chamado
        age: Idade do usuário (valor inteiro)
        gender: Sexo ou identidade de gênero (masculino, feminino, outro, etc.)
        body_type: Tipo corporal do usuário (magro, médio, forte, plus size)
        style_preference: Estilo pessoal (casual, ousado, discreto, confortável, etc.)
        notes: Observações adicionais (livre)

    Returns:
        Dicionário com status de sucesso ou erro e mensagem explicativa
    """
    # Validação de campos obrigatórios
    required_fields = {
        "name": name,
        "age": age,
        "gender": gender,
        "body_type": body_type
    }

    missing_fields = [field for field, value in required_fields.items() if value is None]

    if missing_fields:
        return {
            "success": False,
            "error": f"Faltam os seguintes dados obrigatórios: {', '.join(missing_fields)}"
        }

    if not isinstance(age, int) or age <= 0:
        return {
            "success": False,
            "error": "A idade deve ser um número inteiro positivo."
        }

    # Gêneros possíveis (não exaustivo, apenas validação leve)
    allowed_genders = ["masculino", "feminino", "outro", "prefiro não dizer"]
    if gender.lower() not in allowed_genders:
        return {
            "success": False,
            "error": f"Gênero inválido. Valores aceitos: {', '.join(allowed_genders)}"
        }

    # Simulação de persistência no banco (exemplo apenas)
    print(f"Salvando perfil do usuário...")
    print(f"Nome: {name}, Idade: {age}, Gênero: {gender}, Tipo corporal: {body_type}, Estilo: {style_preference}, Observações: {notes}")

    # Aqui entraria a lógica real de persistência no Firestore, PostgreSQL, etc.

    return {
        "success": True,
        "message": f"Perfil de {name} salvo com sucesso.",
        "data": required_fields
    }
