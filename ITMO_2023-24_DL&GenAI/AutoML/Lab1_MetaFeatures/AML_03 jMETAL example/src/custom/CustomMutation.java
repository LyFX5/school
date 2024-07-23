package custom;

import java.util.function.UnaryOperator;

import org.uma.jmetal.operator.mutation.MutationOperator;
import org.uma.jmetal.solution.Solution;

public class CustomMutation<T> implements MutationOperator<Solution<T>> {

	public CustomMutation(UnaryOperator<T> function, double mutationProbability) {
		this.function = function;
		this.mutationProbability = mutationProbability;
	}

	private static final long serialVersionUID = 1L;
	UnaryOperator<T> function;
	double mutationProbability;

	@Override
	public Solution<T> execute(Solution<T> source) {
		T result = function.apply(source.variables().get(0));
		return new CustomSolution<T>(result);
	}

	@Override
	public double getMutationProbability() {
		return mutationProbability;
	}

}
