vector<double> coeffs(xs.begin(), xs.end());
poly = [this](double x) { double sum = 0; for (int i = 0; i < coeffs.size(); i++) sum += coeffs[i] * pow(x, i); return sum; };
ncoeff = coeffs.size();
return find_zero(coeffs);