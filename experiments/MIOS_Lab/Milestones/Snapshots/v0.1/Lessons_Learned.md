## MIOS Lessons
The Graph is backend independent.

Never allow backend implementation details into Graph.

Endpoints are semantic.

Never store PD inlet numbers in Endpoints.

Runtime implementations belong to RuntimeResolver.

Modules do not know implementation.

Realizers are translators.

They do not own Graph logic.

Backend launch configuration is separate from realization.

Realizing a patch and launching a patch are different responsibilities.

Architecture before implementation.

Every successful experiment came from proving one responsibility before integrating it.