from unittest import TestCase
from chatterbot.adapters.output import OutputAdapter

class OutputAdapterTestCase(TestCase):
    """
    This test case is for the OutputAdapter base class.
    Although this class is not intended for direct use,
    this test case ensures that exceptions requiring
    basic functionality are triggered when needed.
    """

    def setUp(self):
        super(OutputAdapterTestCase, self).setUp()
        self.adapter = OutputAdapter()

    def test_process_response(self):
        with self.assertRaises(OutputAdapter.AdapterMethodNotImplementedError):
            self.adapter.process_response('', 0)
