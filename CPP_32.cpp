```double fractional_part = modf(x, &x);
if(fractional_part > 0.005 || fractional_part < -0.005) x += fractional_part;
return round(x*100.0)/100.0;