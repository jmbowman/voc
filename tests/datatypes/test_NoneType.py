from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class NoneTypeTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = None
            x.thing = 42
            print('Done.')
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = None
            y = x.thing
            print('Done.')
            """)


class UnaryNoneTypeOperationTests(UnaryOperationTestCase, TranspileTestCase):
    values = ['None']

    not_implemented = [
    ]


class BinaryNoneTypeOperationTests(BinaryOperationTestCase, TranspileTestCase):
    values = ['None']

    not_implemented = [
        'test_add_bytearray',
        'test_add_class',
        'test_add_complex',
        'test_add_frozenset',

        'test_and_bytearray',
        'test_and_class',
        'test_and_complex',
        'test_and_frozenset',

        'test_eq_bytearray',
        'test_eq_class',
        'test_eq_complex',
        'test_eq_frozenset',

        'test_floor_divide_bytearray',
        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_ge_bytearray',
        'test_ge_class',
        'test_ge_complex',
        'test_ge_frozenset',

        'test_gt_bytearray',
        'test_gt_class',
        'test_gt_complex',
        'test_gt_frozenset',

        'test_le_bytearray',
        'test_le_class',
        'test_le_complex',
        'test_le_frozenset',

        'test_lshift_bytearray',
        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_frozenset',

        'test_lt_bytearray',
        'test_lt_class',
        'test_lt_complex',
        'test_lt_frozenset',

        'test_modulo_bytearray',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',

        'test_ne_bytearray',
        'test_ne_class',
        'test_ne_complex',
        'test_ne_frozenset',

        'test_or_bytearray',
        'test_or_class',
        'test_or_complex',
        'test_or_frozenset',

        'test_power_bytearray',
        'test_power_class',
        'test_power_complex',
        'test_power_frozenset',

        'test_rshift_bytearray',
        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_frozenset',

        'test_subscr_bytearray',
        'test_subscr_class',
        'test_subscr_complex',

        'test_subtract_bytearray',
        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_frozenset',

        'test_true_divide_bytearray',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_frozenset',

        'test_xor_bytearray',
        'test_xor_class',
        'test_xor_complex',
        'test_xor_frozenset',
    ]


class InplaceNoneTypeOperationTests(InplaceOperationTestCase, TranspileTestCase):
    values = ['None']

    not_implemented = [
        'test_add_bytearray',
        'test_add_class',
        'test_add_complex',
        'test_add_frozenset',

        'test_and_bytearray',
        'test_and_class',
        'test_and_complex',
        'test_and_frozenset',

        'test_floor_divide_bytearray',
        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_lshift_bytearray',
        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_frozenset',

        'test_modulo_bytearray',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_or_bytearray',
        'test_or_class',
        'test_or_complex',
        'test_or_frozenset',

        'test_power_bool',
        'test_power_bytearray',
        'test_power_bytes',
        'test_power_class',
        'test_power_complex',
        'test_power_dict',
        'test_power_float',
        'test_power_frozenset',
        'test_power_int',
        'test_power_list',
        'test_power_none',
        'test_power_set',
        'test_power_str',
        'test_power_tuple',

        'test_rshift_bytearray',
        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_frozenset',

        'test_subtract_bytearray',
        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_frozenset',

        'test_true_divide_bytearray',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_frozenset',

        'test_xor_bytearray',
        'test_xor_class',
        'test_xor_complex',
        'test_xor_frozenset',
    ]
