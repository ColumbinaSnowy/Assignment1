# Pseudocode (copy these by hand for your photos)

## 1. FrogJmp
```
FUNCTION FrogJmp(X, Y, D)
    distance ← Y − X
    RETURN CEILING(distance / D)        // = (distance + D − 1) DIV D
END FUNCTION
```

## 2. PermCheck
```
FUNCTION PermCheck(A)
    N ← length of A
    seen ← array of N+1 values, all FALSE
    FOR each value IN A
        IF value < 1 OR value > N THEN RETURN 0
        IF seen[value] = TRUE THEN RETURN 0
        seen[value] ← TRUE
    END FOR
    RETURN 1
END FUNCTION
```

## 3. MissingInteger
```
FUNCTION MissingInteger(A)
    N ← length of A
    present ← array of N+2 values, all FALSE
    FOR each value IN A
        IF 1 ≤ value ≤ N THEN present[value] ← TRUE
    END FOR
    FOR k ← 1 TO N+1
        IF present[k] = FALSE THEN RETURN k
    END FOR
END FUNCTION
```

## 4. MaxCounters
```
FUNCTION MaxCounters(N, A)
    counters ← array of N zeros
    base ← 0
    currentMax ← 0
    FOR each op IN A
        IF 1 ≤ op ≤ N THEN
            i ← op − 1
            IF counters[i] < base THEN counters[i] ← base
            counters[i] ← counters[i] + 1
            currentMax ← MAX(currentMax, counters[i])
        ELSE                              // op = N + 1
            base ← currentMax
        END IF
    END FOR
    FOR i ← 0 TO N−1
        IF counters[i] < base THEN counters[i] ← base
    END FOR
    RETURN counters
END FUNCTION
```

## 5. PassingCars
```
FUNCTION PassingCars(A)
    eastCount ← 0
    passing ← 0
    FOR each car IN A
        IF car = 0 THEN
            eastCount ← eastCount + 1
        ELSE
            passing ← passing + eastCount
            IF passing > 1,000,000,000 THEN RETURN −1
        END IF
    END FOR
    RETURN passing
END FUNCTION
```
