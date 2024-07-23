package custom;

import java.util.List;
import java.util.function.BinaryOperator;

import org.uma.jmetal.operator.crossover.CrossoverOperator;
import org.uma.jmetal.solution.Solution;

public class CustomCrossover<T> implements CrossoverOperator<Solution<T>> {

	private static final long serialVersionUID = 1L;

	public final BinaryOperator<T> function;

	public final double crossoverProbability;

	public CustomCrossover(BinaryOperator<T> function, double crossoverProbability) {
		this.function = function;
		this.crossoverProbability = crossoverProbability;
	}

	@Override
	public List<Solution<T>> execute(List<Solution<T>> source) {
		Solution<T> first = source.get(0);
		Solution<T> second = source.get(1);

		T firstVariable = first.variables().get(0);
		T secondVariable = second.variables().get(0);

		T result = function.apply(firstVariable, secondVariable);

		return List.of(new CustomSolution<T>(result));
	}

	@Override
	public double getCrossoverProbability() {
		return crossoverProbability;
	}

	@Override
	public int getNumberOfRequiredParents() {
		return 2;
	}

	@Override
	public int getNumberOfGeneratedChildren() {
		return 1;
	}

}
