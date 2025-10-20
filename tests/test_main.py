from importlib.metadata import entry_points

import blockcraft.main as blockcraft_main


def test_main_calls_run_app(monkeypatch):
    called = []

    def fake_run_app():
        called.append(True)

    monkeypatch.setattr(blockcraft_main, "run_app", fake_run_app)

    blockcraft_main.main()

    assert called, "run_app should be invoked by main()"


def test_blockcraft_console_script_registered():
    console_scripts = entry_points().select(group="console_scripts")
    names_to_values = {entry.name: entry.value for entry in console_scripts}

    assert (
        names_to_values.get("blockcraft") == "blockcraft.main:main"
    ), "blockcraft console script must point to blockcraft.main:main"
