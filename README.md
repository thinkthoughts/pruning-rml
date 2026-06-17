# pruning-rml

A notebook-first exploration of arXiv:2606.14150 and related pruning literature through the lens of Residue Memory Learning (RML).

The repository begins with a simple question:

> When a model is pruned and retrained, what useful structure survives?

The notebooks develop a vocabulary for comparing reset and revision strategies, examining pruning granularity, residue preservation, budget-matched comparisons, revision triggers, revision policies, and benchmark design.

This repository is not a reproduction of the paper's experimental results. Instead, it serves as a computational notebook series for exploring how pruning can be interpreted as a form of revision rather than complete reset.

## Notebook Map

### Context and Comparison

* 00 Context
* 07 Pruning vs Scratch
* 13 Granularity
* 17 Revision Not Reset
* 23 Surviving Residues
* 29 Budget-Matched Comparisons

### Revision Framework

* 31 Revision Triggers
* 37 RML-Guided Pruning
* 41 Pruning Policies
* 43 Policy Evaluation
* 47 Residue Retention

### Lifecycle and Governance

* 53 Revision Lifecycle
* 59 Revision Stability
* 61 Residue Accumulation
* 67 Residue Revision Boundary
* 71 Revision Scheduler
* 73 Revision Queue
* 79 Revision Execution
* 83 Revision Feedback
* 89 Revision Governance

### Toward Experiments

* 97 Revision Architecture
* 101 Repo Retrospective
* 103 Real Pruning Experiments
* 107 Benchmark Design
* 109 Minimum Viable Benchmark

## Central Question

Can pruning preserve useful residues that reduce the need for complete retraining?

The notebooks explore this question through small computational examples, benchmark design exercises, and revision-oriented interpretations of pruning.
