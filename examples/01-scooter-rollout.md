# Scaling a hardware fleet

> **Prompt:** dockless e-scooter rental. Each scooter costs us about €500 and nets around €8 a day in rides, so it pays for itself in roughly two months. Demand in our pilot city is great. We want to order 50,000 scooters and launch in 40 cities this year. Go?

Unedited answer from the blind eval run (case `H01`).

---

**Decision**: Whether to commit roughly €25M (50,000 × €500) to scooters and 40 city launches this year, based on a single pilot city.
**Verdict**: Not as planned. First, find out how long a scooter actually lasts and what it really earns over that life. Then scale in stages. · Confidence: 7/10

The demand you're seeing is real, and it's the strongest point in your favour. The trouble is that "pays for itself in two months" only holds if the scooter is still on the street after two months. You haven't said what your fleet's lifespan is. In 2018–19, scooters from the first wave were widely reported to last only a few months, and in some cities only about a month. That figure comes from general knowledge, not from my precedent library, so treat it as unverified.

**Precedents**
☠ Webvan (1996–2001): died of premature scaling and bad unit economics. It contracted about $1B of infrastructure for 26 cities while its first market still wasn't profitable. Matches you on mechanism and business model (heavy owned assets, economics that depend on density). Differs on market.
☠ Bird (from general knowledge, not in the library): scaled into hundreds of cities fast and filed for bankruptcy in 2023. Matches on market, model and mechanism.
✓ Lime (general knowledge): survived the same shakeout. It built more durable scooters, cut back to fewer cities, and reported being profitable on an adjusted basis.
✓ Instacart: avoided Webvan's trap by using assets other people already owned.

**Agreement**: The demand looks real. What's unproven is the economics over a scooter's whole life.
**Real disagreement**: The Expansionist says winning city permits early is a moat, since many cities cap fleet sizes or run tenders. The Devil's advocate says permits can also be pulled: Paris banned shared scooters in 2023 after a referendum.
**Assumption that matters most**: How long a scooter lives, multiplied by its true net per day. The net has to come after repairs, theft, vandalism, charging, moving scooters around, insurance and city fees, and it has to hold up in winter and with a much bigger fleet. → The cheapest test is to group your pilot scooters by deployment date and count how many are still earning at 60, 120 and 180 days.
**Closest precedent**: Webvan. You become Webvan if the money goes out before the lifespan is proven. You become Lime if you prove durability first and enter cities where you can reach high density.

**Next step (48 h)**: Pull the pilot data by scooter: deployment date, retirement date, total net revenue and total repair cost. Ask the supplier whether you can turn the 50,000 order into about 5,000 firm units plus options on the rest.
**Kill criterion**: By 31 March 2027, run 3–5 cities with fleet sizes like the ones you plan. If projected lifetime net per scooter is below about €1,000 (2× unit cost, my estimate), or the median scooter lives less than 9 months, don't place the big order.

▸ The Crew
- Nix · Devil's advocate: against. €8/day × 60 days is break-even only if the scooter survives. The pilot may also be inflated by novelty and having no competitors.
- Root · First principles: depends. Lease or finance the fleet, or partner on it, rather than paying €25M up front.
- Nova · Expansionist: for doing it in stages. City permits are scarce and worth something.
- Pip · Outsider: 40 cities in one year means 40 sets of rules, 40 local teams and 40 winters.
- Tack · Executor: 1,250 scooters per city need warehouses, mechanics and chargers, and you don't have any of that yet.
- Finance (added because €25M is at stake): a two-month payback with no lifespan data isn't a payback figure.

I can also make a visual report or a decision log if you want one.
