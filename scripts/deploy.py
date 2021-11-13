from scripts.helpful_scripts import get_account
from brownie import Voting
def deploy_voting():
    account=get_account()
    Candidates =["Putin","Modi"]
    voting=Voting.deploy(Candidates,{"from":account})
    # (name,votes)=voting.candidates(0)
    # print(name)
    return voting
def main():
    deploy_voting() 