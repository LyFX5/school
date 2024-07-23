package custom;

import org.uma.jmetal.solution.AbstractSolution;
import org.uma.jmetal.solution.Solution;

public class CustomSolution<T> extends AbstractSolution<T> {

	private static final long serialVersionUID = 1L;

	public CustomSolution(T object) {
		super(1, 1);
		variables().set(0, object);
	}

	@Override
	public Solution<T> copy() {
		return new CustomSolution<T>(variables().get(0));
	}

}
