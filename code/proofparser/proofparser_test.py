from proofparser import ProofParser

import pytest

@pytest.fixture
def parser():
    return ProofParser()

def test_tokenize(parser):
    tokens = parser.tokenize('P(x)')
    ids = [token.id for token in tokens]
    assert ids == ['P', '(', 'x', ')', 'END']

def test_parses_simple_expression(parser):
    result = parser.parse('P(x)')
    assert result == ('P', 'x')
