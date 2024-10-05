# Test file for InvalidUseOfOverload checker - testing what mypy doesn't pick up

from typing import Awaitable, overload, Union

class testingOverload:
    @overload
    def double(a: str)  -> Awaitable[int]:
        ...

    @overload
    def double(a: int):
        ...

    async def double(a: Union[str, int]) -> int:
        if isinstance(a, str):
            return len(a)*2
        return a * 2


    @overload
    def doubleAgain(a: str):
        ...

    @overload
    def doubleAgain(a: int):
        ...

    async def doubleAgain(a: Union[str, int]) -> int:
        if isinstance(a, str):
            return len(a)*2
        return a * 2