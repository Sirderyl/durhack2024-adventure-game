#!/usr/bin/env python3

from reactpy import component, html, run, hooks

from stories import STORIES
from story import Story

@component
def App():
    story, setStory = hooks.use_state(None)
    def mk_story_handler(story: Story):
        def exec(_):
            setStory(story) # type: ignore
        return exec

    return html.div(
        html.h1("Hello, world!"),
        html.p("This is a story game."),
        html.ul(
            *(html.li(
                html.button(
                    {"onClick": mk_story_handler(STORIES['self_worth'])},
                    story.title
                )
            ) for story in STORIES.values())
        ) if story is None else html.h2(story.title)
    )

run(App)
# from story import Story

# def choose_story():
#     print("Choose a story:")
#     by_index: list[Story] = []
#     for index, id in enumerate(STORIES):
#         story = STORIES[id]
#         by_index.append(story)
#         print(f"{index + 1}. {story.title}")

#     while True:
#         try:
#             choice = int(input("Enter the number of the story you want to play: "))
#             if choice < 1:
#                 raise ValueError()
#             story = by_index[choice - 1]
#             break
#         except (ValueError, IndexError):
#             print("Invalid choice. Please try again.")

#     return story



# def main():
#     # story = choose_story()
#     # TODO: Placeholder
#     story = STORIES['self_worth']

#     story.print_intro()

# if __name__ == '__main__':
#     main()
