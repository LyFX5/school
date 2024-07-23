package numeric;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.function.ToDoubleFunction;

import org.uma.jmetal.problem.doubleproblem.impl.AbstractDoubleProblem;
import org.uma.jmetal.solution.doublesolution.DoubleSolution;

public class WrappedDoubleProblem extends AbstractDoubleProblem {

	private static final long serialVersionUID = 1L;
	public final ToDoubleFunction<double[]> error;

	public WrappedDoubleProblem(int numberOfVariables, ToDoubleFunction<double[]> error, double l, double r) {
		super();
		setNumberOfVariables(numberOfVariables);
		setNumberOfObjectives(1);
		setNumberOfConstraints(0);
		setName(getClass().getSimpleName() + "(" + error.toString() + ")");

		List<Double> lowerLimit = new ArrayList<>(numberOfVariables);
		List<Double> upperLimit = new ArrayList<>(numberOfVariables);

		for (int i = 0; i < getNumberOfVariables(); i++) {
			lowerLimit.add(l);
			upperLimit.add(r);
		}

		setVariableBounds(lowerLimit, upperLimit);

		this.error = error;
	}

	public static double[] toArray(DoubleSolution solution) {
		return toArray(solution.variables());
	}

	public static double[] toArray(Collection<Double> collection) {
		return collection.stream().mapToDouble(d -> d).toArray();
	}

	@Override
	public DoubleSolution evaluate(DoubleSolution solution) {
		double[] array = solution.variables().stream().mapToDouble(d -> d).toArray();
		double value = error.applyAsDouble(array);
		solution.objectives()[0] = value;
		return solution;
	}

}
