def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
   assert expected_result in actual_result, \
        f"expected {expected_result}, got {actual_result}"
test_input_text( '123', '123')