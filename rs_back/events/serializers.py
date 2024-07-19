from rest_framework import serializers

from rs_back.events.models import ClassicEvent, Questionnaire


class ClassicEventsSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор для всех записей
    @details Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = ClassicEvent
        fields = ('id', 'title', 'photo')


class ClassicEventByIdSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор для одной записи
    @details Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = ClassicEvent
        fields = (
            'id', 'title', 'description',
            'photo', 'photo_album_url',
            'documents_url', 'location',
            'event_date', 'social_media_mention',
            'registration_link'
        )


class QuestionnaireByIdSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор для одной записи
    @details Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = Questionnaire
        fields = (
            'id', 'searcher_fio', 'searcher_bmstu_group',
            'participants_count', 'required_competencies',
            'searcher_VK', 'additional',
        )


class QuestionnairesSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор для одной записи
    @details Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = Questionnaire
        fields = ('id', 'searcher_fio', 'classic_event')
