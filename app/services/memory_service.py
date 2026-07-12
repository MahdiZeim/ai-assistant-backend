conversation = []


def add_message(role: str, content: str):
    conversation.append(
        {
            "role": role,
            "content": content
        }
    )


def get_history():
    return conversation