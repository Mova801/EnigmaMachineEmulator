from src.commands.command import Command

MAIN_SCREEN_COMMANDS: tuple[Command, ...] = (
    Command('conf', 'configuration', 'Configure the Enigma Machine.', lambda x: x),
    Command('emu', 'emulate', 'Start the Enigma Machine emulation.', lambda x: x)
)
