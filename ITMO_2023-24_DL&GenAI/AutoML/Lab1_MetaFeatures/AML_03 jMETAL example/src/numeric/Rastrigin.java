package numeric;

import java.util.function.ToDoubleFunction;

public class Rastrigin implements ToDoubleFunction<double[]> {
	public final int n;
	public static final double A = 10;

	public Rastrigin(int n) {
		this.n = n;
	}

	@Override
	public double applyAsDouble(double[] x) {
		double sum = A * n;

		for (int i = 0; i < n; i++) {
			sum += x[i] * x[i] - A * Math.cos(2.0 * Math.PI * x[i]);
		}

		return sum;
	};
}
