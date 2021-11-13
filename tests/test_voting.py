from scripts.deploy import deploy_voting
from scripts.helpful_scripts import get_account,LOCAL_BLOCKCHAIN_ENVIRONMENTS
import pytest
from brownie import network
def test_voting():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    voting =deploy_voting()
    chairman=get_account()
    account1=get_account(index=1)
    account2=get_account(index=2)
    account3=get_account(index=3)
    voting.vote(0,{"from":chairman})
    voting.vote(0,{"from":account1})
    voting.vote(0,{"from":account2})
    voting.vote(1,{"from":account3})
    voting.getWinnerName({"from":chairman}).wait(1)
    print(voting.winnerName())
    assert voting.winnerName()=="Putin"
