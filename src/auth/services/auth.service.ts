import { Injectable } from '@nestjs/common';
import { UserService } from 'src/users/services/user.service';

@Injectable()
export class AuthService {
  constructor(private readonly userService: UserService) {}

  async login(stdNum: string, password: string) {
    const existingUser = await this.userService.findUser({ where: { stdNum } });

    if (existingUser) {
      return this.userService.updateUser(stdNum, password);
    } else {
      return this.userService.createUser(stdNum, password);
    }
  }
}
