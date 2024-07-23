package custom;

import java.util.function.Supplier;
import java.util.function.ToDoubleFunction;

import org.uma.jmetal.problem.Problem;
import org.uma.jmetal.solution.Solution;

public class WrappedCustomProblem<T> implements Problem<Solution<T>> {

	private static final long serialVersionUID = 1L;
	public final ToDoubleFunction<T> error;
	public final Supplier<T> generator;

	public WrappedCustomProblem(ToDoubleFunction<T> error, Supplier<T> generator) {
		this.error = error;
		this.generator = generator;
	}

	@Override
	public int getNumberOfVariables() {
		return 1;
	}

	@Override
	public int getNumberOfObjectives() {
		return 1;
	}

	@Override
	public int getNumberOfConstraints() {
		return 0;
	}

	@Override
	public String getName() {
		return getClass().getSimpleName() + "(" + error.toString() + ")";
	}

	@Override
	public Solution<T> evaluate(Solution<T> solution) {
		T object = solution.variables().get(0);
		double value = error.applyAsDouble(object);
		solution.objectives()[0] = value;
		return solution;
	}

	@Override
	public Solution<T> createSolution() {
		return new CustomSolution<T>(generator.get());
	}

}
