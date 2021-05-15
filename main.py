from OpenAIController import OpenAIController
from PexelsController import PexelsController

sample_description = "Velox is a real-time platform that helps remote teams keeping organized chats. In Velox, " \
                     "you can create new conversations for different topics. "


if __name__ == '__main__':
    # execute only if run as the entry point into the program

    openAI = OpenAIController()
    openAI.get_tagline(sample_description)

    openAI.get_sample_testimonial_bio(sample_description)

