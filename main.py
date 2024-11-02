#!/usr/bin/env python3

from reactpy import component, html, run, hooks

from stories import STORIES
from story import Story

@component
def StorySummary(story: Story):
    return html.div(
        html.h2(story.title),
        html.p(story.introduction),
        html.p(story.character_description),
    )

@component
def Game(story: Story):
    return html.div(
        StorySummary(story),
    )

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
        ) if story is None else Game(story)
    )

run(App)
