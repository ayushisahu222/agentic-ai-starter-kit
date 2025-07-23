#!/usr/bin/env python
# src/latest_ai_development/main.py
import sys
from crew import TimeCrew

def run():
  """
  Run the crew.
  """
  inputs = {
    'topic': 'What is the current time?',
  }
  TimeCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()