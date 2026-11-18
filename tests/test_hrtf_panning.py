import pytest
from audio import hrtf_panning as mod

CASES = [
    ("spherical_pair", "m.spherical(0.0, 0.0) == (0.0, 0.0)"),
    ("spherical_elev", "m.spherical(0.0, 30.0) == (0.0, 30.0)"),
    ("head_center", "m.head_compensation(10.0, 0.0) == approx(10.0)"),
    ("head_comp", "m.head_compensation(10.0, 5.0) == approx(5.0)"),
    ("delay_mid", "m.binaural_delay(1.0, 343.0) == approx(1.0)"),
    ("delay_zero", "m.binaural_delay(0.0, 343.0) == approx(0.0)"),
    ("near_one", "m.near_field(1.0) == approx(1.0)"),
    ("order_pair", "m.order_hrtf('hrtf', 'reverb') == ('hrtf', 'reverb')"),
    ("resample_same", "m.resample_filter(48000, 48000) == approx(1.0)"),
    ("resample_double", "m.resample_filter(48000, 24000) == approx(2.0)"),
    ("source_id", "m.per_source(3) == 3"),
    ("personalize_mid", "m.personalize(1.0, 2.0) == approx(2.0)"),
    ("crossfade_mid", "m.crossfade(0.0, 1.0, 0.5) == approx(0.5)"),
    ("pop_limited", "m.pop_suppress(1.0, 2.0) == approx(1.0)"),
    ("pop_zero", "m.pop_suppress(1.0, 0.0) == approx(0.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
