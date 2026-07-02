from hammer import detect_hammer
from doji import detect_doji
from engulfing import detect_engulfing

def pattern_manager(df):
    df = detect_hammer(df)
    df = detect_doji(df)
    df = detect_engulfing(df)
    return df