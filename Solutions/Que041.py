# enumerate function takes a collection (eg:tuple) and return it as enumerate object.


def itinerary(flights, start_point, current):
    if not flights:
        return current + [start_point]

    updated = None
    for i, (c1, c2) in enumerate(flights):
        if start_point == c1:
            sub_itinerary = itinerary(flights[:i] + flights[i + 1:], c2, current + [c1]
                                      )
            if sub_itinerary:
                if not updated or "".join(sub_itinerary) < "".join(updated):
                    updated = sub_itinerary

    return updated


print(itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], "A", []))
print(itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'),('HKO', 'ORD')], "YUL", []))