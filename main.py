#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


def main() -> None:

    screen_width = 80
    screen_height = 50

    map_width = 80
    map_heght = 45

    tileset = tcod.tileset.load_tilesheet(
        "chars.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    center_x = int(screen_width / 2)
    center_y = int(screen_height / 2)
    player = Entity(center_x, center_y, "@", (255, 255, 255))
    npc = Entity(center_x - 5, center_y, "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_heght)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)


    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "The Dankest Roguelike",
        vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console ,context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
