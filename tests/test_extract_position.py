from src.extract_position import extract_position


def test_extract_position():
    result_1 = extract_position(
        '|error| numerical calculations could not converge.')
    result_2 = extract_position(
        '|update| the positron location in the particle accelerator is x:21.432')
    assert result_1 is None
    assert result_2 == '21.432'
