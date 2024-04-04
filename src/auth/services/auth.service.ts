import { Injectable } from '@nestjs/common';
import { UserService } from 'src/users/services/user.service';

@Injectable()
export class AuthService {
  constructor(private readonly userService: UserService) {}

  login(stdNum: string, password: string) {
    return this.userService.createUser(stdNum, password);
  }
}
