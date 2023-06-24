var = 17
var_left = var << 2
var_right = var >> 2
print(var, var_left, var_right)

# 17 << 2 → 17 * 4
# (17 multiplied by 2 to the power of 2) → 68
# (shifting to the left by two bits is the same as integer multiplication by four)

# 17 >> 2 → 17 // 4
# (17 floor-divided by 2 to the power of 2) →
# (shifting to the right by one bit is the same as integer division by four)
